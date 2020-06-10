import random
from typing import AsyncIterable

import faust

from faustify.app import faustify_app
from faust import StreamT


class PageViewRecord(faust.Record):
    id: str
    user: str


topic_page_view = faustify_app.topic('faustify-user-views', value_type=PageViewRecord)

table_page_views = faustify_app.Table('user-pv', default=int)
table_user_views = faustify_app.Table('user-uv', default=int)


@faustify_app.agent(topic_page_view)
async def process_page_views(views):
    async for view in views.group_by(PageViewRecord.id):
        table_page_views[view.id] += 1
        print(view.id)


@faustify_app.timer(interval=1.0)
async def auto_send_page_views():
    await process_page_views.send(
        value=PageViewRecord(
            id=f"{random.randint(0, 20900)}",
            user=f"user-{random.randint(0, 20900)}",
        ),
    )


@faustify_app.timer(interval=30)
async def auto_stats_page_views():
    await process_page_views.send(

        value=PageViewRecord(
            id=f"{random.randint(0, 20900)}",
            user=f"user-{random.randint(0, 20900)}",
        ),
    )


@faustify_app.page('/count/')
@faustify_app.table_route(table=table_page_views, query_param='user')
async def get_count(web, request):
    user = request.query['user']
    return web.json({
        'user': table_page_views[user],
    })

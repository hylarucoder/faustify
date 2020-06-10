from faustify.app import faustify_app


@faustify_app.timer(30.0)
async def my_periodic_task():
    print('THIRTY SECONDS PASSED')

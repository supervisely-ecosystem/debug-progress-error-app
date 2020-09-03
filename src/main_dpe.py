import time
import supervisely_lib as sly

my_app = sly.AppService()


@my_app.callback("run")
@sly.timeit
def run(api: sly.Api, task_id, context, state, app_logger):
    progress = sly.Progress("Processing", 10, app_logger)
    for i in range(10):
        time.sleep(1)
        progress.iter_done_report()
    raise RuntimeError("Debug error")


def main():
    initial_events = [{"state": None, "context": None, "command": "run"}]

    # Run application service
    my_app.run(data={}, state={}, initial_events=initial_events)


if __name__ == "__main__":
    sly.main_wrapper("main", main)
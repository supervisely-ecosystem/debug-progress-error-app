import time
import supervisely_lib as sly

# my_app = sly.AppService()


# @my_app.callback("run")
@sly.timeit
def run():
    progress = sly.Progress("Processing", 10)
    for i in range(10):
        time.sleep(1)
        progress.iter_done_report()
    raise RuntimeError("Debug error")


def main():
    # initial_events = [{"state": None, "context": None, "command": "run"},
    #                   {"state": None, "context": None, "command": "stop"}]

    # Run application service
    # my_app.run(data={}, state={}, initial_events=initial_events)
    run()


if __name__ == "__main__":
    sly.main_wrapper("main", main)
import time
import supervisely_lib as sly


@sly.timeit
def main():
    
    # check_dir = "/mount_folder"
    # if sly.fs.dir_exists(check_dir):
    #     files = sly.fs.list_dir_recursively(check_dir)
    #     for path in files:
    #         sly.logger.info(f"File: {path}")
        
    
    progress = sly.Progress("Processing", 1000)
    for i in range(1000):
        time.sleep(1)
        progress.iter_done_report()
        if i % 20 == 0:
            sly.logger.info("I'M STILL ALIVE")
    # raise RuntimeError("Debug error")


if __name__ == "__main__":
    sly.main_wrapper("main", main)

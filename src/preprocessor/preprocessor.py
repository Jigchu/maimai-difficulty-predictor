from preprocessor.settings import preprocessorSettings

def main():
    filter()
    normalize()
    split_charts()
    return

def filter():
    version_filter = preprocessorSettings["version_filter"]
    level_filter = preprocessorSettings["level_filter"]
    diffifculty_filter = preprocessorSettings["difficulty_filter"]
    filter_utage = preprocessorSettings["filter_utage"]

    return

def normalize():
    return

def split_charts():
    return

if __name__ == "__main__":
    main()

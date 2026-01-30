
def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_videos(videos):
    pass


def main():
    while True:
        print("\n Youtube Manager | choise an option")
        print("1. List all youtube videos: ")
        print("2. Add a youtube video ")
        print("3. Update an youtube video details ")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        choise = input("Enter your choise")

        match choise:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid choise")
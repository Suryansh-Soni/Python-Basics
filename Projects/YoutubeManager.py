import json

def load_data():
    try:
        with open('youtube.txt', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data_helper(video):
    with open('youtube.txt', 'w') as f:
        json.dump(video, f)

def list_all_videos(video):
    if not video:
        print("No videos found.")
    else:
        for i, v in enumerate(video, start=1):
            print(f"{i}. {v['Name']} | Duration: {v['Time']}")

def add_video(video):
    vName = input("Enter Video Name: ")
    time = input("Enter video time: ")
    video.append({'Name': vName, 'Time': time})
    save_data_helper(video)
    print("Video added successfully!")

def update_video(video):
    pass
def delete_video(video):
    pass


def main():
    video = load_data()

    while True:
        print("\nYoutube Manager | Choose an Option")
        print("1. List all youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete the video")
        print("5. Exit the app")

        choice = input("Enter your Choice: ")

        match choice:
            case '1':
                list_all_videos(video)
            case '2':
                add_video(video)
            case '3':
                update_video(video)
            case '4':
                delete_video(video)
            case '5':
                break
            case _:
                print("Invalid Choice.")

if __name__ == "__main__":
    main()
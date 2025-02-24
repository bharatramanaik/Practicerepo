import json

def load_data():
    try:
        with open("video.txt", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_helper(videos):
    with open("video.txt", 'w') as f:
        json.dump(videos,f)

def list_all(videos):
    print("list of videos: ")
    for index, vid in enumerate(videos, start=1):
        print(f"{index}. Name {vid['name']} duration: {vid['time']}")
    print('\n')

def create(videos):
    name = input("enter video name: ")
    time = input("enter duration: ")
    videos.append({'name':name, 'time':time})
    save_helper(videos)

def update(videos):
    list_all(videos)
    index = int(input("enter the index of video to be updated"))
    if 1 <= index <= len(videos):
        name = input("enter new name: ")
        time = input("enter new time: ")
        videos[index - 1] = {'name':name, 'time': time}
        save_helper(videos)
    else :
        print("index out of bound")


def delete(videos):
    list_all(videos)
    index = int(input("enter the index of video to be updated"))
    if 1 <= index <= len(videos):
        del videos[index - 1]
        save_helper(videos)
        print("deleted ")
    else :
        print("index out of bound")

def main():
    videos = load_data()
    while True:
        print("1.list all")
        print("2.create")
        print("3.update")
        print("4.delete")
        choice = int(input("enter your choice: "))
        match(choice):
            case 1 : list_all(videos)
            case 2 : create(videos)
            case 3 : update(videos)
            case 4 : delete(videos)
            case _ : break

if __name__ == "__main__":
    main()
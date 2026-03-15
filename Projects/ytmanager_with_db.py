import sqlite3
con=sqlite3.connect('youtube_video.db')
cursor=con.cursor()
cursor.execute('''
Create table if not exists Video(
               id Integer primary key,
               name text not null,
               time text not null
               )
''')


def list_video():
    cursor.execute("select * from video ")
    for row in cursor.fetchall():
        print(row)


def add_video(name,time):
    cursor.execute("insert into video(name,time) values(?,?)",(name,time))
    con.commit()


def update_video(video_id,new_name,new_time):
     cursor.execute("update video set name = ?,time= ? where id= ? ",(new_name,new_time,video_id))
     con.commit()
def del_video(video_id):
    cursor.execute("delete from video where id=?",(video_id,))
    con.commit()

def main():
    while True:

        print("\nYoutube Manager | Choose an Option")
        print("1. List all youtube video")
        print("2. Add a youtube video")
        print("3. Update a youtube video detail")
        print("4. Delete the video")
        print("5. Exit the app")

        choice = input("Enter your Choice: ")

        if(choice=="1"):
            list_video()
        elif(choice=="2"):
            name=input("Enter Video Name: ")
            time=input("Enter the time :")
            add_video(name,time)
        elif(choice=="3"):
            videoId=input("Enter Video Id: ")
            name=input("Enter Video Name: ")
            time=input("Enter the time :")
            update_video(videoId,name,time)
        elif(choice=="4"):
            videoId=input("Enter Video Id to delete : ")
            name=input("Enter Video Name: ")
            time=input("Enter the time: ")
            del_video(videoId)
        elif(choice=="5"):
            break
        else:
            print("invalid choice.")
    con.close()


if __name__=="__main__":
    main()
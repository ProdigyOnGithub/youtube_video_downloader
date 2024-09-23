import customtkinter
from pytube import YouTube
import os

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

app = customtkinter.CTk()
app.geometry("500x400")
app.title("Youtube Video Downloader")


def run(name, url):
    try:
        pop = customtkinter.CTkToplevel(app)
        pop.title("Done")
        pop.geometry("400x100")
        my_video = YouTube(url)

        print(my_video.title)
        print(my_video.thumbnail_url)
        my_video = my_video.streams.get_highest_resolution()
        downloads_path = os.path.expanduser("~") + "/Downloads/"
        if name is None:
            name = my_video.title
        my_video.download(downloads_path, filename=f"{name}.mp4")

        label = customtkinter.CTkLabel(master=pop, text="Video successfully downloaded in the downloads folder")
        label.pack(pady=12, padx=10)
    except:
        pop = customtkinter.CTkToplevel(app)
        pop.title("Error")
        pop.geometry("300x100")

        label = customtkinter.CTkLabel(master=pop, text="Unable to download video. Check for problems")
        label.pack(pady=12, padx=10)


def main():
    frame = customtkinter.CTkFrame(master=app)
    frame.place(x=40, y=20, width=420, height=340)

    label = customtkinter.CTkLabel(master=frame, text="Youtube Video Downloader")
    label.pack(pady=12, padx=10)

    entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Name")
    entry1.pack(pady=12, padx=10)

    entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="URL")
    entry2.pack(pady=12, padx=10)

    btn = customtkinter.CTkButton(master=frame, text="Download", command=lambda: run(entry1.get(), entry2.get()))
    btn.pack(pady=12, padx=10)


main()

app.mainloop()

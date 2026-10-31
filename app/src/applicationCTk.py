import customtkinter as ctk
import tools
from downloaderYtb import DownloaderYtb
import threading



class ApplicationCTk(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Window settings
        self.geometry("500x420")
        self.title("Audiolog | YouTube Downloader")
        self.resizable(False, False)
        self._set_appearance_mode('dark')

        # set M4A as default var-radio
        self.selected_format = 'mp3'
        # ******************************************

        # Widgets
        self.title_label = ctk.CTkLabel(
            self,
            text="Audiolog",
            font=('Arial', 24, 'bold'),
            text_color=('yellow')
        )
        self.title_label.pack(pady=(30, 20))

        self.input_url = ctk.CTkEntry(
            self,
            placeholder_text='Paste your link here...',
            width=400,
            height=40,
            font=('Arial', 12, 'italic')
        )
        self.input_url.pack(pady=10)
        self.format_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.format_frame.pack(pady=10)

        self.format_var = ctk.IntVar(value=1)

        self.radio_MP3 = ctk.CTkRadioButton(
            self.format_frame,
            text='MP3',
            text_color=('yellow'),
            fg_color=('white'),
            variable=self.format_var,
            value=1,
            font=('Arial', 11)
        )
        self.radio_MP3.pack(side="left", padx=15)

        self.radio_M4A = ctk.CTkRadioButton(
            self.format_frame,
            text='M4A',
            text_color=('yellow'),
            fg_color=('white'),
            variable=self.format_var,
            value=0,
            font=('Arial', 11),
        )
        self.radio_M4A.pack(side="left", padx=15)

        self.button = ctk.CTkButton(
            self,
            command=self.download_button,
            text='Download',
            text_color=('black'),
            fg_color=('yellow'),
            width=200,
            height=40,
            font=('Arial', 12, 'bold')
        )
        self.button.pack(pady=20)

        self.progress_bar = ctk.CTkProgressBar(self, width=400)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(10, 5))

        self.status_label = ctk.CTkLabel(
            self,
            text="Ready for download",
            font=('Arial', 10),
            text_color="gray"
        )
        self.status_label.pack(pady=(0, 20))
        # ******************************************


    # worker
    def _worker_thread(self, url, selected_format):
        try:
            audio_dwd = DownloaderYtb(url, self.format_var.get())

            self.after(0, lambda: self.progress_bar.set(0.5))
            self.after(0, lambda: self.status_label.configure(
                text=f"Downloading in {self.selected_format}...",
                text_color="orange"
            ))

            if self.selected_format == 'm4a':
                audio_dwd.download_m4a()
            elif self.selected_format == 'mp3':
                audio_dwd.convert_to_mp3()

            self.after(0, lambda: self.progress_bar.set(1.0))
            self.after(0, lambda: self.status_label.configure(
                text="Download complete!",
                text_color="green"
            ))
        except Exception as err:
            self.after(0, lambda: self.status_label.configure(
                text=f"ERROR _worker_thread(): {err}",
                text_color="red"
            ))
        finally:
            self.after(0, lambda: self.button.configure(state="normal"))


    def download_button(self):
        try:
            url_video = self.input_url.get()
            if tools.confirm_request(url_video) == None or tools.confirm_request(url_video) == False:
                self.status_label.configure(text='Request Error or Invalid URL! Try again', text_color='red')
                self.status_label.update_idletasks()
            else:
                file_format = self.format_var.get()
                self.selected_format = 'm4a' if file_format == 0 else 'mp3'
                thread = threading.Thread(
                    target=self._worker_thread,
                    args=(url_video, self.selected_format),
                    daemon=True            
                )
                thread.start()
        except Exception as err:
            print(f'ERROR download_button: {err}')



if __name__ == "__main__":
    app = ApplicationCTk()
    app.mainloop()
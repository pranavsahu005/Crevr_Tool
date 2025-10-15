
👉 [Crevr_Tool](https://github.com/pranavsahu005/Crevr_Tool)

# ⚙️ Crevr Tool

Crevr Tool is an advanced **web-based image processing and editing application** built with **Django** and **HTML/CSS**. It is inspired by Canva, providing simple yet powerful tools to help users upload, edit, and enhance images directly from the browser.

---

## 🚀 Key Features
- 🖼️ **Upload & Manage Images** seamlessly
- 🎨 **Image Editing Tools**  
  - Convert to Grayscale  
  - Compress Image Files  
  - Resize or Rotate Images  
  - Crop Selected Areas
- 💾 **Automatic Local Storage** using Django’s media management
- 👤 **User Authentication (Signin Page)**
- ⚡ **Fast, Lightweight & Responsive UI**
- 🧩 **Organized Project Architecture** with reusable templates and static assets

---

## 🧠 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django (Python) |
| Frontend | HTML, CSS |
| Database | SQLite3 |
| Image Processing | Pillow |
| Version Control | Git & GitHub |
| Deployment | Localhost / GitHub Pages (for static preview) |

---

## 🗂️ Project Structure
```

Crevr Tool/
├── tools/
│   ├── grayscale/
│   │   ├── **init**.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── templates/
│   │   └── static/
│   ├── manage.py
│   └── db.sqlite3
└── README.md

````

---

## ⚙️ Installation & Setup

### 1️⃣ Clone this repository
```bash
git clone https://github.com/pranavsahu005/Crevr_Tool.git
````

### 2️⃣ Navigate to project directory

```bash
cd Crevr_Tool/tools
```

### 3️⃣ Create & activate virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate
```

### 4️⃣ Install required dependencies

```bash
pip install django pillow
```
```numpy and open cv
pip install opencv-python
```

### 5️⃣ Run the development server

```bash
python manage.py runserver
```

### 6️⃣ Open your browser

```
http://127.0.0.1:8000/
```

---

## 💡 Future Enhancements

* 🧰 Add advanced filters (brightness, contrast, blur)
* ☁️ Integrate cloud storage (AWS, Firebase)
* 📱 Improve mobile responsiveness with Tailwind CSS
* 💾 Enable project save & download functionality
* ✨ Add drag-and-drop editor and multi-image workspace

---

## 📸 Screenshots

*(Add your screenshots here)*
Recommended path:

```
tools/static/image/
```

Example (Markdown Preview):

```markdown
![Editor Interface](tools/static/image/sample_editor.png)
![Grayscale Output](tools/static/image/sample_gray.png)
```

---

## 🤝 Contributing

We welcome contributions from the community!
To contribute:

1. Fork the repo
2. Create your feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to your branch (`git push origin feature-name`)
5. Open a Pull Request

---

## 🧑‍💻 Author

**👋 Pranav Sahu**
💼 Developed with ❤️ using Django
🌐 [GitHub Profile](https://github.com/pranavsahu005)

---

## 🔁 Quick Update Command

Whenever you make changes locally and want to update GitHub:

```bash
cd "C:/Users/user/OneDrive/Desktop/Crevr Tool" && git add . && git commit -m "Auto update" && git push origin main
```

---

⭐ **If you like this project, consider giving it a star on GitHub!**

````

---

✅ **Next steps:**
1. Copy all of the above.  
2. Open your project folder → `Crevr Tool`  
3. Create or replace file `README.md`  
4. Save it.  
5. Run:
   ```bash
   git add README.md
   git commit -m "Updated README for Crevr Tool"
   git push origin main
````

🔗 Check now:

Open → https://github.com/pranavsahu005/Crevr_Tool

You’ll see all your folders and files uploaded correctly.

⚙️ For future updates:

Whenever you make new changes or add files, just run this one-line update command:
```
cd "C:/Users/user/OneDrive/Desktop/Crevr Tool" && git add . && git commit -m "Auto update" && git push origin main
```


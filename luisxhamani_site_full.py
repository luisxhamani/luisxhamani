import zipfile
import os

# Création de la structure de dossiers
base_dir = '/mnt/data/luisxhamani_site_full'
os.makedirs(f'{base_dir}/images', exist_ok=True)
os.makedirs(f'{base_dir}/videos', exist_ok=True)

# Création des fichiers HTML et CSS
files_content = {
    f'{base_dir}/index.html': """<!DOCTYPE html>
<html lang=\"fr\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Photographe et Vidéaste à Grenoble</title>
    <link rel=\"stylesheet\" href=\"style.css\">
</head>
<body>
    <header>
        <div class=\"logo\">
            <img src=\"images/logo.png\" alt=\"Logo\">
        </div>
        <nav>
            <a href=\"#services\">Services</a>
            <a href=\"#portfolio\">Portfolio</a>
            <a href=\"#contact\">Contact</a>
        </nav>
    </header>

    <section id=\"hero\">
        <h1>Bonjour, je suis Luis</h1>
        <p>Photographe et vidéaste basé à Grenoble</p>
    </section>

    <section id=\"services\">
        <h2>Mes Services</h2>
        <div class=\"service\">
            <h3>Reportage Photo</h3>
            <p>Captation d'événements, portraits, et plus.</p>
        </div>
        <div class=\"service\">
            <h3>Reportage Vidéo</h3>
            <p>Films d'événements, clips, et plus.</p>
        </div>
        <div class=\"service\">
            <h3>Drone</h3>
            <p>Prises de vue aériennes pour une perspective unique.</p>
        </div>
    </section>

    <section id=\"portfolio\">
        <h2>Portfolio</h2>
        <div class=\"gallery\">
            <img src=\"images/photo1.jpg\" alt=\"Photo 1\">
            <img src=\"images/photo2.jpg\" alt=\"Photo 2\">
            <img src=\"images/photo3.jpg\" alt=\"Photo 3\">
        </div>
        <video controls>
            <source src=\"videos/ma_video.mp4\" type=\"video/mp4\">
            Votre navigateur ne supporte pas la lecture de vidéos.
        </video>
    </section>

    <section id=\"contact\">
        <h2>Contact</h2>
        <p>Pour toute demande, contactez-moi à l'adresse suivante :</p>
        <a href=\"mailto:luisxhamani@example.com\">luisxhamani@example.com</a>
    </section>

    <footer>
        <p>&copy; 2025 Luis Xhamani</p>
    </footer>
</body>
</html>""",

    f'{base_dir}/style.css': """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

header {
    background-color: #333;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

header .logo img {
    width: 100px;
}

header nav {
    margin-top: 10px;
}

header nav a {
    color: #fff;
    margin: 0 15px;
    text-decoration: none;
    text-transform: uppercase;
}

header nav a:hover {
    text-decoration: underline;
}

#hero {
    background: url('images/ma_photo.jpg') no-repeat center center/cover;
    color: #fff;
    text-align: center;
    padding: 100px 20px;
}

#hero h1 {
    font-size: 3em;
}

#hero p {
    font-size: 1.5em;
}

#services {
    padding: 50px 20px;
    text-align: center;
    background-color: #fff;
}

#services h2 {
    margin-bottom: 30px;
}

.service {
    margin-bottom: 30px;
}

.service h3 {
    font-size: 2em;
    margin-bottom: 10px;
}

#portfolio {
    padding: 50px 20px;
    background-color: #f9f9f9;
    text-align: center;
}

#portfolio h2 {
    margin-bottom: 30px;
}

.gallery {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin-bottom: 30px;
}

.gallery img {
    width: 30%;
    border-radius: 8px;
}

video {
    width: 80%;
    max-width: 800px;
    border-radius: 8px;
}

#contact {
    padding: 50px 20px;
    background-color: #fff;
    text-align: center;
}

#contact h2 {
    margin-bottom: 20px;
}

#contact a {
    color: #333;
    text-decoration: none;
    font-weight: bold;
}

#contact a:hover {
    text-decoration: underline;
}

footer {
    background-color: #333;
    color: #fff;
    text-align: center;
    padding: 10px 0;
}"""
}

# Création de fichiers images et vidéo vides
with open(f'{base_dir}/images/ma_photo.jpg', 'wb') as f:
    f.write(b'')
with open(f'{base_dir}/images/photo1.jpg', 'wb') as f:
    f.write(b'')
with open(f'{base_dir}/images/photo2.jpg', 'wb') as f:
    f.write(b'')
with open(f'{base_dir}/images/photo3.jpg', 'wb') as f:
    f.write(b'')
with open(f'{base_dir}/images/logo.png', 'wb') as f:
    f.write(b'')
with open(f'{base_dir}/videos/ma_video.mp4', 'wb') as f:
    f.write(b'')

# Écriture des fichiers HTML et CSS
for path, content in files_content.items():
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

# Création du ZIP
zip_path = '/mnt/data/luisxhamani_site_full.zip'
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, _, files in os.walk(base_dir):
        for file in files:
            zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), base_dir))

zip_path
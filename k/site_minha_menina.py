html_content = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Para a mulher que eu mais amei</title>
  <style>
    body {
      margin: 0;
      font-family: 'Segoe UI', sans-serif;
      background: linear-gradient(to bottom, #fff0f5, #ffe4e1);
      color: #333;
      padding: 20px;
    }
    header {
      text-align: center;
      margin-bottom: 30px;
    }
    h1 {
      font-size: 2.5em;
      color: #b30059;
    }
    .text-block {
      max-width: 800px;
      margin: 20px auto;
      background: #ffffffcc;
      padding: 20px;
      border-radius: 16px;
      box-shadow: 0 4px 10px rgba(0,0,0,0.1);
      line-height: 1.6;
    }
    .gallery {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 15px;
      margin-top: 30px;
    }
    .gallery img {
      max-width: 250px;
      border-radius: 12px;
      box-shadow: 0 2px 6px rgba(0,0,0,0.1);
    }
    .videos {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 20px;
      margin-top: 40px;
    }
    iframe {
      width: 100%;
      max-width: 560px;
      height: 315px;
      border: none;
      border-radius: 10px;
    }
    audio {
      display: block;
      margin: 20px auto;
    }
    footer {
      text-align: center;
      margin-top: 40px;
      color: #666;
    }
  </style>
</head>
<body>
  <header>
    <h1>Para a mulher que eu mais amei</h1>
    <p><em>Minha menina</em></p>
  </header>

  <div class="text-block">
    <p>Não sei quantas almas eu tenho<br>
    Mudei e continuo mudando.<br>
    De uma coisa sei, não importa quantas<br>
    porque meu amor por você<br>
    É como se existissem dois de mim apenas pra te amar.</p>

    <p>A criança quando nasce chora, dentre outros motivos, ela chora também porque pela primeira vez entrou em contato com a luz da vida. Assim como ela, quando eu te encontrar, chorarei por estar encontrando a luz da minha vida, a mulher que, mesmo longe, me ensinou a ser eu. Chorarei no teu abraço, e vou me encantar ao ver que sua perfeição fora da tela do celular, ao ver que seu rosto perto do meu, seus olhos de encontro com a luz deixando o seu castanho cada vez mais claro e sutil. Ao ver seu cabelo brilhar quando está no sol e seus cachos balançarem com o vento, ao ver você simplesmente de pé na minha frente me olhando também emocionada só por me ver.</p>

    <p>Te vendo da cabeça aos pés,<br>
    Percebo que o amor não é ilusório,<br>
    Percebo que a vida não é robótica <br>
    Olhando pra você, da cabeça aos pés <br>
    Eu vi que o capítulo que falta na minha vida, <br>
    Não é escrita e sim vivida com você.</p>

    <p>Talvez o céu seja fictício e Deus me mandou você pra ensinar o que é amar e o que é felicidade, talvez ele tenha te mandado com sua luz para me iluminar ou talvez eu esteja apenas viajando e você, na verdade nem existe. Tamanha perfeição nesse mundo deveria ser crime, e eu sentenciado à prisão por te amar com intensidade e de modo que nem eu sabia que podia.</p>
  </div>

  <div class="gallery">
    <!-- Substitua pelas imagens reais -->
    <img src="imagem1.jpg" alt="Foto 1" />
    <img src="imagem2.jpg" alt="Foto 2" />
    <img src="imagem3.jpg" alt="Foto 3" />
  </div>

  <div class="videos">
    <iframe src="https://www.youtube.com/embed/7lQi82loFlI?autoplay=1&loop=1&playlist=7lQi82loFlI" allow="autoplay"></iframe>
    <iframe src="https://photos.app.goo.gl/pnEAmG7PdUMSB8Tk6" title="Vídeo 1"></iframe>
    <iframe src="https://photos.app.goo.gl/XxudXeTiC8B1vLgb9" title="Vídeo 2"></iframe>
    <iframe src="https://photos.app.goo.gl/71TTP5hidvQWwP5u8" title="Vídeo 3"></iframe>
  </div>

  <footer>
    <p>Com amor, do Gabriel para sua menina 💗</p>
  </footer>
</body>
</html>
"""

with open('site_minha_menina.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Arquivo 'site_minha_menina.html' criado com sucesso!")

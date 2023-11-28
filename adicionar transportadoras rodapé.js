document.addEventListener('DOMContentLoaded', function() {

const listaAtual = document.querySelector('#rodape-envios > ul');

const listaDeImagens = [
    "https://cdn.awsli.com.br/2664/2664239/arquivos/jadlog.jpg",
    "https://cdn.awsli.com.br/2664/2664239/arquivos/correios.jpg"
];

for (let i = 0; i < listaDeImagens.length; i++) {
    const imagem = listaDeImagens[i];
    const liElement = document.createElement('li');
    const imgElement = document.createElement('img');
    imgElement.src = imagem;
    liElement.appendChild(imgElement);
    listaAtual.appendChild(liElement);
}

});

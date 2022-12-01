$(document).ready( function(){
    if( $(window).width() < 767 && $('#cabecalho .carrinho .qtd-carrinho').length ){
      $('.atalhos-mobile li.fundo-principal').append( $('#cabecalho .carrinho .qtd-carrinho').clone() );
    }
  });
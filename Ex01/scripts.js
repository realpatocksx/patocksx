
var noticias = {}
const botao = document.querySelector('.botao')
botao.addEventListener('click', function(event){
    event.preventDefault()
    let nome_noticia = document.querySelector('#nomedanoticia').value
    let categoria_noticia = document.querySelector('#categorianoticia').value
    let descricao_noticia = document.querySelector('#descricaonoticia').value
    
    //alert('Nome da Noticia: '  + nome_noticia + 'Tipo da Categoria: ' + categoria_noticia + 'Descricao:' + descricao_noticia)

    noticias = {
        'Nome da Noticia: ': nome_noticia,
        'Tipo da Categoria: ': categoria_noticia, 
        'Descricao da Noticia: ': descricao_noticia 
    }
    console.log(noticias)
});
console.log(noticias)

document.querySelector('#paraghoras')
document.querySelector('#imghoras')

var hora = 13

if (hora >= 11) {
    alert('manha')
} else if (hora <= 12) {
    alert('tarde')
} else if (hora < 18) {
    alert('noite')
}
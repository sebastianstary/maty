function generateSeatsOptions() {
    var seatsselect = document.getElementById('sedadlo');
    const rows = 10;
    const sedadla = 12;
    seatsselect.innerHTML = '';
                for (var row = 1; row <= rows; row++) {
                    for (var seat = 1; seat <= sedadla; seat++) {
                        var sedadlo = row + '-' + seat;
                            var option = document.createElement('option');
                            option.text = 'Řada: '+ row + ' Sedadlo: ' + seat;
                            option.value = sedadlo;
                            seatsselect.appendChild(option);
                    }
                }
    }
    // Volání funkce pro generování možností při načtení stránky
window.onload = function() {
    generateSeatsOptions();
};

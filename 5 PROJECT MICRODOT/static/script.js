// MENGAMBIL DATA IP DARI SERVER
async function fetchIpData() {
    try {
        const response = await fetch('/updateData');
        const data = await response.json();
        return data.ip;
    } catch (error) {
        console.error('Error fetching IP data:', error);
        return '0.0.0.0'; // MENAMPILKAN IP 0.0.0.0 JIKA TERJADI KESALAHAN ATAU ERROR
    }
}

// MEMPERBARUI TAMPILAN IP PADA HALAMAN WEB
async function updateIpDisplay() {
    const displayElement = document.querySelector('.ip h3');
    try {
         const ipAddress = await fetchIpData();
        displayElement.textContent = `${ipAddress}`; // MENAMPILKAN ALAMAT IP DI ELEMEN YANG DIPILIH
        setTimeout(updateIpDisplay, 6000); // MENGULANGI PEMBARUAN SETIAP 6 DETIK
    } catch (error) {
        console.error('Error updating IP display:', error);
    }
}
updateIpDisplay(); // MEMANGGIL FUNCTION UNTUK MENGUPDATE IP
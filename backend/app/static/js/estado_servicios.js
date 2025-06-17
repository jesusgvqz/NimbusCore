async function cargarEstadoServicios() {
    try {
        const response = await fetch('/api/estado_servicios/');
        const data = await response.json();

        const panel = document.getElementById('panel-servicios');
        panel.innerHTML = '';

        data.forEach(servidor => {
            const div = document.createElement('div');
            div.className = 'mb-4 p-3 border rounded';

            let html = `<h4>${servidor.servidor} (${servidor.ip})</h4>`;

            if (servidor.error) {
                html += `<p style="color: red;">Error: ${servidor.error}</p>`;
            } else {
                if (servidor.servicios_activos.length === 0) {
                    html += '<p>No hay servicios activos.</p>';
                } else {
                    html += '<ul>';
                    servidor.servicios_activos.forEach(servicio => {
                        html += `<li>${servicio}</li>`;
                    });
                    html += '</ul>';
                }
            }

            div.innerHTML = html;
            panel.appendChild(div);
        });
    } catch (err) {
        console.error('Error cargando estado:', err);
        document.getElementById('panel-servicios').innerHTML = '<p style="color:red;">Error al cargar los datos.</p>';
    }
}

// Carga la primera vez y después cada 30 segundos
cargarEstadoServicios();
setInterval(cargarEstadoServicios, 30000);
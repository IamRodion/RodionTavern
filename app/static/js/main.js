let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions={
    columnDefs: [
        // { className:'centered', targets: [0, 1, 2, 3, 4, 5, 6, 7] },
        { orderable: false, targets: [3, 4]},
        { searchable: false, targets: [0, 7] }
    ],
    pageLength: 6,
    destroy: true,
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    await list_trades();
    dataTable=$('#table_trades').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const list_trades = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/list_trades/');
        const data = await response.json();

        let content = '';
        data.trades.forEach((trade, index) => {
            content += `
            <tr>
                <td>${index + 1}</td>
                <td><img src="/static/${trade.item_icon}" class="icons" alt="icon" srcset=""><br>${trade.item_name}</td>
                <td>${trade.amount_primary_stat}<br>${trade.item_primary_stat}</td>
                <td>${trade.amount_secondary_stat}<br>${trade.secondary_stat}</td>
                <td>${trade.bonus_1}<br>${trade.bonus_2}</td>
                <td><img src="/static/img/others/elite.webp" class="icons" alt="" srcset=""><br>${trade.elite ? 'Si' : 'No'}</td>
                <td>${trade.enchant ?? 'No'}</td>
                <td><img src="/static/img/others/gold.png" class="icons" alt="" srcset=""><br>${trade.price}</td>
            </tr>
            `;
        });
        const table_body = document.getElementById("table_body_trades");
        table_body.innerHTML = content;
        // table_body_trades.innerHTML = content;
    } catch (ex) {
        console.log(ex);
        // alert(ex);
    }
};

window.addEventListener('load', async () => {
    await initDataTable();
});
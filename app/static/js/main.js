let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        // { className:'centered', targets: [0, 1, 2, 3, 4, 5, 6, 7] },
        { orderable: false, targets: [3, 4] },
        { searchable: false, targets: [0, 7] }
    ],
    pageLength: 12,
    destroy: true,
};

const initDataTable = async () => {
    if (dataTableIsInitialized) {
        dataTable.destroy();
    }
    await list_trades();
    dataTable = $('#table_trades').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const list_trades = async () => {
    try {
        const response = await fetch('http://127.0.0.1:8000/list_trades/');
        const data = await response.json();

        let content = '';
        data.trades.forEach((trade, index) => {

            // Primary stat with colors
            // let primaryStatData = `<td>${trade.amount_primary_stat}<br>`;
            // if (trade.item_primary_stat === 'Magic') {
            //     primaryStatData += `<span class="magic">${trade.item_primary_stat}</span></td>`;
            // } else if (trade.item_primary_stat === 'Melee') {
            //     primaryStatData += `<span class="melee">${trade.item_primary_stat}</span></td>`;
            // } else if (trade.item_primary_stat === 'Distance') {
            //     primaryStatData += `<span class="distance">${trade.item_primary_stat}</span></td>`;
            // } else {
            //     primaryStatData += `<span>${trade.item_primary_stat}</span></td>`;
            // }

            let primaryStatData = `<td>`;
            if (trade.item_primary_stat === 'Magic') {
                primaryStatData += `<span class="badge rounded-pill magic">${trade.amount_primary_stat} ${trade.item_primary_stat}</span></td>`;
            } else if (trade.item_primary_stat === 'Melee') {
                primaryStatData += `<span class="badge rounded-pill melee">${trade.amount_primary_stat} ${trade.item_primary_stat}</span></td>`;
            } else if (trade.item_primary_stat === 'Distance') {
                primaryStatData += `<span class="badge rounded-pill distance">${trade.amount_primary_stat} ${trade.item_primary_stat}</span></td>`;
            } else {
                primaryStatData += `<span>${trade.item_primary_stat}</span></td>`;
            }            


            // Secondary stat with colors
            // let secondaryStatData = `<td>${trade.amount_secondary_stat}<br>`;
            // if (trade.secondary_stat === 'Magic') {
            //     secondaryStatData += `<span class="magic">${trade.secondary_stat}</span></td>`;
            // } else if (trade.secondary_stat === 'Melee') {
            //     secondaryStatData += `<span class="melee">${trade.secondary_stat}</span></td>`;
            // } else if (trade.secondary_stat === 'Distance') {
            //     secondaryStatData += `<span class="distance">${trade.secondary_stat}</span></td>`;
            // } else if (trade.secondary_stat === 'Spirit') {
            //     secondaryStatData += `<span class="spirit">${trade.secondary_stat}</span></td>`;
            // } else if (trade.secondary_stat === 'Defense') {
            //     secondaryStatData += `<span class="defense">${trade.secondary_stat}</span></td>`;
            // } else {
            //     secondaryStatData += `<span>${trade.item_primary_stat}</span></td>`;
            // }

            let secondaryStatData = `<td>`;
            if (trade.secondary_stat === 'Magic') {
                secondaryStatData += `<span class="badge rounded-pill magic">${trade.amount_secondary_stat} ${trade.secondary_stat}</span></td>`;
            } else if (trade.secondary_stat === 'Melee') {
                secondaryStatData += `<span class="badge rounded-pill melee">${trade.amount_secondary_stat} ${trade.secondary_stat}</span></td>`;
            } else if (trade.secondary_stat === 'Distance') {
                secondaryStatData += `<span class="badge rounded-pill distance">${trade.amount_secondary_stat} ${trade.secondary_stat}</span></td>`;
            } else if (trade.secondary_stat === 'Spirit') {
                secondaryStatData += `<span class="badge rounded-pill spirit">${trade.amount_secondary_stat} ${trade.secondary_stat}</span></td>`;
            } else if (trade.secondary_stat === 'Defense') {
                secondaryStatData += `<span class="badge rounded-pill defense">${trade.amount_secondary_stat} ${trade.secondary_stat}</span></td>`;
            } else {
                secondaryStatData += `<span>${trade.item_primary_stat}</span></td>`;
            }



            // Elite with icon
            let eliteData = `<td><img src="/static/img/others/`;
            if (trade.elite) {
                eliteData += `elite.webp" class="icons" alt="Icon Elite"><br>Yes</td>`;
            } else {
                eliteData += `elite-no.png" class="icons" alt="Icon no Elite"><br>No</td>`;
            }

            // Enchant with icon
            let enchantData = '<td><img src="/static/img/elements/';
            if (trade.enchant === 'Mana') {
                enchantData += `mana.png" class="icons" alt="${trade.enchant}"><br>${trade.enchant}</td>`;
            } else if (trade.enchant === 'Ice') {
                enchantData += `ice.png" class="icons" alt="${trade.enchant}"><br>${trade.enchant}</td>`;
            } else if (trade.enchant === 'Nature') {
                enchantData += `nature.png" class="icons" alt="${trade.enchant}"><br>${trade.enchant}</td>`;
            } else if (trade.enchant === 'Energy') {
                enchantData += `energy.png" class="icons" alt="${trade.enchant}"><br>${trade.enchant}</td>`;
            } else if (trade.enchant === 'Fire') {
                enchantData += `fire.png" class="icons" alt="${trade.enchant}"><br>${trade.enchant}</td>`;
            } else if (trade.enchant === 'Physical') {
                enchantData += `physical.png" class="icons" alt="${trade.enchant}"><br>${trade.enchant}</td>`;
            } else {
                enchantData = `<td>${trade.enchant ?? 'No'}</td>`;
            }

            content += `
            <tr>
                <td>${index + 1}</td>
                <td><img src="/static/${trade.item_icon}" class="icons" alt="icon" srcset=""><br>${trade.item_name}</td>
                ${primaryStatData}
                ${secondaryStatData}
                <td>${trade.bonus_1}<br>${trade.bonus_2}</td>
                ${eliteData}
                ${enchantData}
                <td><img src="/static/img/others/gold.png" class="icons" alt="" srcset=""><br>${trade.price}</td>
                <td><button type="button" class="btn btn-primary">Info</button></td>
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
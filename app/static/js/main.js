let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    // responsive: true,
    columnDefs: [
        // { className:'centered', targets: [0, 1, 2, 3, 4, 5, 6, 7] },
        { orderable: false, targets: [3, 4, 8] },
        { searchable: false, targets: [0, 7, 8] },
        { visible: false, targets: [0, 9] },
    ],
    pageLength: 20,
    destroy: true,
    order: [[0, 'asc']],
    language: {
        searchPlaceholder: "Item, Stat, Bonus, or Seller"
    },
    // stateSave: true,
    // pagingType: 'numbers',
    // scrollCollapse: true,
    // scrollY: '250px'
    // scrollX: true,
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
        const response = await fetch('/json_trades/');
        const data = await response.json();

        let content = '';
        data.trades.forEach((trade, index) => {

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
                enchantData = `<td>${trade.enchant ?? 'Not Enchanted'}</td>`;
            }

            let primary_and_secondary_statdata = `<tr>`;
            if (trade.item_primary_stat == trade.secondary_stat){
                amount_stat = trade.amount_primary_stat + trade.amount_secondary_stat
                if (trade.item_primary_stat === 'Magic') {
                    primary_and_secondary_statdata += `<td><span class="badge rounded-pill magic">${amount_stat} ${trade.item_primary_stat}</span></td></tr>`;
                } else if (trade.item_primary_stat === 'Melee') {
                    primary_and_secondary_statdata += `<td><span class="badge rounded-pill melee">${amount_stat} ${trade.item_primary_stat}</span></td></tr>`;
                } else if (trade.item_primary_stat === 'Distance') {
                    primary_and_secondary_statdata += `<td><span class="badge rounded-pill distance">${amount_stat} ${trade.item_primary_stat}</span></td></tr>`;
                } else {
                    primary_and_secondary_statdata += `<td><span>${trade.item_primary_stat}</span></td></tr>`;
                }
                primary_and_secondary_statdata += `<tr><td><span class="badge rounded-pill stamina">${trade.item_stamina} Stamina</span></td></tr>`
                
            } else {
                primary_and_secondary_statdata += `${primaryStatData}</tr>
                <tr><td><span class="badge rounded-pill stamina">${trade.item_stamina} Stamina</span></td></tr>
                <tr>${secondaryStatData}</tr>`
            }


            content += `
            <tr>
                <td>${index + 1}</td>
                <td><img src="/static${trade.item_icon}" class="icons" alt="icon" srcset=""><br>${trade.item_name}</td>
                ${primaryStatData}
                ${secondaryStatData}
                <td>${trade.bonus_1}<br>${trade.bonus_2}</td>
                ${eliteData}
                ${enchantData}
                <td><img src="/static/img/others/gold.png" class="icons" alt="" srcset=""><br>${trade.price}</td>
                <td><button class="btn btn-sm btn-primary" data-bs-toggle="offcanvas" data-bs-target="#offcanvas${trade.id}">Info</button>
                    <div class="offcanvas offcanvas-end" data-bs-scroll="true" tabindex="-1" id="offcanvas${trade.id}">
                        <div class="offcanvas-header">
                            <h5 class="offcanvas-title">${trade.item_name}</h5>
                            <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
                        </div>
                        
                        <div class="row justify-content-md-center">
                            <div class="col col-11">
                                <div class="offcanvas-body">
                                    <table class="table table-striped border-primary table-bordered align-middle">
                                        <thead>
                                            <tr class="table-primary text-center">
                                                <th><img src="/static${trade.item_icon}" class="icons" alt="item-icon" srcset=""><br>${trade.item_name}</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr><td>Req. level ${trade.item_level}</td></tr>
                                            <tr><td>${trade.armour} Armour</td></tr>
                                            ${primary_and_secondary_statdata}
                                            <tr><td>${trade.bonus_1}<br>${trade.bonus_2}</td></tr>
                                            <tr>${enchantData}</tr>
                                            <tr>${eliteData}</tr>
                                            <tr><td><img src="/static/img/others/gold.png" class="icons" alt="Gold Icon"> ${trade.price}</td></tr>
                                            <tr><td>Seller: <b>${trade.username}</b></td></tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </td>
                <td>${trade.username}</td>
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
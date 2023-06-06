export default function Consumables({consumableInfo}){
    let consumables = []

    consumableInfo.forEach(element => {
        consumables.push(
            <div>
                <div class="total">
                  <div class="key">
                    Total
                  </div>
                  <div class="value">
                    { element.number }
                  </div>
                </div>
                <div class="remainingConsumable">
                  <input name="remainingConsumable"
                         type="text"
                         id="{{ key }}"
                         onChange="storeItem('{{ key }}', '{{ character.name }}')"/>
                  
                  <label for="remainingConsumable">
                    { element.name }
                  </label>
                </div>
            </div>
        )
    });
    return(
        <div>
            {consumables}
        </div>
    )
}
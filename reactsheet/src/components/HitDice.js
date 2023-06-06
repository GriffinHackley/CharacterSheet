import '../css/HitDice.css'

export default function HitDice({hitDice}){
    return (
        <div class="hitDice">
            <div class="totalHD">
              <div class="key">Total Hit Dice</div>
              <div class="value">
                {hitDice}
              </div>
            </div>
            <input
              type="text"
              id="remainingHD"
              onChange="storeItem('remainingHD', '{ character.name }')"
            />
            <script>
              {/* getItem('remainingHD', '{character.name}') */}
            </script>
            <label for="remainingHD">Hit Dice</label>
          </div>
    )
}
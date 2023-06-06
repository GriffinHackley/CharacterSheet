import '../css/TempHP.css'

export default function TempHP(){
    return (
        <div class="temporary">
            <input
              type="text"
              id="temphp"
              onChange="storeItem('temphp', '{ character.name }')"
            />
            <script>
              {/* getItem('temphp', '{character.name}') */}
            </script>
            <label for="temphp">Temporary Hit Points</label>
          </div>
    )
}
import '../css/Conditions.css'

export default function Conditions() {
  return (
    <div class="conditions">
      <textarea
        id="conditions"
        onChange="storeItem('conditions', '{ character.name }')"
      />

      <label>Conditions</label>
      <script>
        {/* getItem('conditions', '{character.name}') */}
      </script>
    </div>
  );
}

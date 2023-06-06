import "../css/Resistances.css";

export default function Resistances() {
  return (
    <div class="resistances">
      <textarea
        id="resistances"
        onChange="storeItem('resistances', '{ character.name }')"
      />
      <label>Resistances</label>
      <script>
        {/* getItem('resistances', '{character.name}') */}
      </script>
    </div>
  );
}

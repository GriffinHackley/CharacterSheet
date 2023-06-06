import "../css/CurrentHP.css";

export default function CurrentHP({ HP }) {
  return (
    <div class="current">
      <div class="maxHP">
        <div class="key">Max Hit Points</div>
        <div class="value">
          {HP}
        </div>
      </div>
      <input
        type="text"
        id="currentHealth"
        onChange="storeItem('currentHealth', '{ character.name }')"
      />
      <script>
        {/* getItem('currentHealth', '{character.name}') */}
      </script>
      <label>Current Hit Points</label>
    </div>
  );
}

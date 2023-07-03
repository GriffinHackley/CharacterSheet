import "../../../css/DeathSaves.css";

export default function DeathSaves() {
  return (
    <div className="deathsaves">
      <div className="marks">
        <div className="deathsuccesses">
          <label>Successes</label>
          <div className="bubbles">
            <input name="deathsuccess1" type="checkbox" />
            <input name="deathsuccess2" type="checkbox" />
            <input name="deathsuccess3" type="checkbox" />
          </div>
        </div>
        <div className="deathfails">
          <label>Failures</label>
          <div className="bubbles">
            <input name="deathfail1" type="checkbox" />
            <input name="deathfail2" type="checkbox" />
            <input name="deathfail3" type="checkbox" />
          </div>
        </div>
      </div>
      <label>Death Saves</label>
    </div>
  );
}

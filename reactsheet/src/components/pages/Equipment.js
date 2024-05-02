import { useLocation } from "react-router-dom";

export default function Equipment() {
  const location = useLocation();
  const { equipmentInfo } = location.state;

  return (
    <section className="equipment">
      <div className="equipmentRightPane">
        <div className="money">
          <div>
            <div className="copper">
              <label for="copper">Copper</label>
              <input name="copper" id="copper" />
            </div>
            <div className="silver">
              <label for="silver">Silver</label>
              <input name="silver" id="silver" />
            </div>
          </div>
          <div>
            <div className="gold">
              <label for="gold">Gold</label>
              <input name="gold" id="gold" />
            </div>
            <div className="platinum">
              <label for="platinum">Platinum</label>
              <input name="platinum" id="platinum" />
            </div>
          </div>
        </div>
        <textarea
          className="extraEquipment"
          placeholder="Equipment list here"
          id="extraEquipment"
        />
      </div>
    </section>
  );
}

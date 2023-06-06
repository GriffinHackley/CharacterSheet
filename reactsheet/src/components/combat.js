export default function Combat({ combatInfo }) {
  console.log(combatInfo);
  //TODO: Fix get Items
  return (
    <section class="combat">
      <div class="combatHeader">
        <div class="tooltip centered armorclass" data-tooltip="{ source }">
          <div class="value">
            {combatInfo.AC.value}
          </div>
          <div class="key">Armor Class</div>
        </div>
        <div class="tooltip centered CMD" data-tooltip="{ source }">
          <div class="value">
            {combatInfo.CMD.value}
          </div>
          <div class="key">CMD</div>
        </div>
        <div class="tooltip centered initiative" data-tooltip="{ source }">
          <div class="value">
            {combatInfo.Initiative.value}
          </div>
          <div class="key">Initiative</div>
        </div>
        <div class="tooltip centered speed" data-tooltip="{ source }">
          <div class="value">
            {combatInfo.Speed.value}
          </div>
          <div class="key">Speed</div>
        </div>
      </div>
      <div class="hp">
        <div class="otherHp">
          <div class="hitdice">
            <div class="totalHD">
              <div class="key">Total Hit Dice</div>
              <div class="value">
                {combatInfo.hitDice}
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
          <div class="deathsaves">
            <div class="marks">
              <div class="deathsuccesses">
                <label>Successes</label>
                <div class="bubbles">
                  <input name="deathsuccess1" type="checkbox" />
                  <input name="deathsuccess2" type="checkbox" />
                  <input name="deathsuccess3" type="checkbox" />
                </div>
              </div>
              <div class="deathfails">
                <label>Failures</label>
                <div class="bubbles">
                  <input name="deathfail1" type="checkbox" />
                  <input name="deathfail2" type="checkbox" />
                  <input name="deathfail3" type="checkbox" />
                </div>
              </div>
            </div>
            <label>Death Saves</label>
          </div>
          <div class="conditions">
            {/* </textarea id="conditions"
                          onChange="storeItem('conditions', '{ character.name }')"/> */}

            <label>Conditions</label>
            <script>
              {/* getItem('conditions', '{character.name}') */}
            </script>
          </div>
        </div>
        <div class="currentTotalHealth">
          <div class="current">
            <div class="maxHP">
              <div class="key">Max Hit Points</div>
              <div class="value">
                {combatInfo.HP}
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
        </div>
      </div>
    </section>
  );
}

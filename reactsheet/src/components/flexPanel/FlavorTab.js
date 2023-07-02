export default function FlavorTab({ flavorInfo }) {
  let backstory = "This is the backstory";
  return (
    <div class="tabContent" data-tab="main-flavor">
      <section class="flavor">
        <div class="backstory">
          <h2>Backstory</h2>
          {backstory}
        </div>
        <div class="columnContainer">
          {/* <div class="personalityTraits">
              <h2>
                Personality Traits
              </h2>
              <div class="flavorText">
                {% with character.flavor.personalityTraits|split as lines %}
                  {% for line in lines %}
                    <p>
                      {{ line }}
                    </p>
                  {% endfor %}
                {% endwith %}
              </div>
                  </div>
                  <div class="ideals">
              <h2>
                Ideals
              </h2>
              <div class="flavorText">
                {% with character.flavor.ideals|split as lines %}
                  {% for line in lines %}
                    <p>
                      {{ line }}
                    </p>
                  {% endfor %}
                {% endwith %}
              </div>
                  </div>
                  <div class="bonds">
              <h2>
                Bonds
              </h2>
              <div class="flavorText">
                {% with character.flavor.bonds|split as lines %}
                  {% for line in lines %}
                    <p>
                      {{ line }}
                    </p>
                  {% endfor %}
                {% endwith %}
              </div>
                  </div>
                  <div class="flaws">
              <h2>
                Flaws
              </h2>
              <div class="flavorText">
                {% with character.flavor.flaws|split as lines %}
                  {% for line in lines %}
                    <p>
                      {{ line }}
                    </p>
                  {% endfor %}
                {% endwith %}
              </div>
                  </div> */}
        </div>
      </section>
    </div>
  );
}

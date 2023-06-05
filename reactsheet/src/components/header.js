export default function Header({headerInfo}){
    // console.log(headerInfo)
    return (
        <header>
            <section class="charname">
                <div>{ headerInfo.name }</div>
            </section>
            <section class="misc">
                <ul>
                  <li>
                    <div class="field">Class & Level</div>
                    <div class="value">{ headerInfo.class } { headerInfo.level }</div>
                  </li>
                  <li>
                    <div class="field">Background</div>
                    <div class="value">{ headerInfo.background }</div>
                  </li>
                  <li>
                    <div class="field">Player Name</div>
                    <div class="value">{ headerInfo.player }</div>
                  </li>
                  <li>
                    <div class="field">Race</div>
                    <div class="value">{ headerInfo.race }</div>
                  </li>
                  <li>
                    <div class="field">Alignment</div>
                    <div class="value">{ headerInfo.alignment }</div>
                  </li>
                  {/* {% if character.config.edition == "Pathfinder" %}
                    <li>
                      <div class="field">Traits</div>
                      <div class="value">{{ character.traits.0 }}, {{ character.traits.1 }}</div>
                    </li>
                  {% endif %} */}
                </ul>
            </section>
        </header>
    )
}
import '../css/Header.css'

export default function Header({headerInfo}){
    let pathfinder = null
    if(headerInfo.edition == "Pathfinder"){
        pathfinder  = (
            <li>
                <div class="field">Traits</div>
                <div class="value">{ headerInfo.traits[0] }, { headerInfo.traits[1] }</div>
            </li>
        )
    }
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
                  {pathfinder}
                </ul>
            </section>
        </header>
    )
}
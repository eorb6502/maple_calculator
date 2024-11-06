function update_skill(){
    const dropdown_val = document.getElementById('skill_check').value;
    const skill_damage = document.getElementById('skill_damage')
    const attack_count = document.getElementById('attack_count')
    const hyper_damage = document.getElementById('hyper_damage')
    const core_reinforce = document.getElementById('core_reinforce')
    const core_ignore_monster_armor = document.getElementById('core_ignore_monster_armor')
    const skill_ignore_monster_armor = document.getElementById('skill_ignore_monster_armor')
    const skill_final_damage = document.getElementById('skill_final_damage')
    const skill_normal_damage = document.getElementById('skill_normal_damage')
    if (dropdown_val==="jikjup"){
        skill_damage.value=""
        attack_count.value=""
        hyper_damage.value=""
        core_reinforce.value=""
        core_ignore_monster_armor.value=""
        skill_ignore_monster_armor.value=""
        skill_final_damage.value=""
        skill_normal_damage.value=""
    }
    else if (dropdown_val==="dawn"){
        const yanus = JSON.parse(localStorage.getItem("yanus_spec"))
        console.log(yanus)
        skill_damage.value=390+10*yanus["skill_level"]
        attack_count.value=6
        hyper_damage.value=0
        core_reinforce.value=0
        core_ignore_monster_armor.value=0
        skill_ignore_monster_armor.value=0
        skill_final_damage.value=yanus["skill_final_damage"]
        skill_normal_damage.value=yanus["skill_normal_damage"]
    }
    else if (dropdown_val==="twilight"){
        const yanus = JSON.parse(localStorage.getItem("yanus_spec"))
        console.log(yanus)
        skill_damage.value=585+15*yanus["skill_level"]
        attack_count.value=6
        hyper_damage.value=0
        core_reinforce.value=0
        core_ignore_monster_armor.value=0
        skill_ignore_monster_armor.value=0
        skill_final_damage.value=yanus["skill_final_damage"]
        skill_normal_damage.value=yanus["skill_normal_damage"]
    }
    else if (dropdown_val==="fountain"){
        const fountain = JSON.parse(localStorage.getItem("fountain_spec"))
        console.log(fountain)
        skill_damage.value=450+15*fountain["skill_level"]
        attack_count.value=4
        hyper_damage.value=0
        core_reinforce.value=0
        core_ignore_monster_armor.value=0
        skill_ignore_monster_armor.value=0
        skill_final_damage.value=yanus["skill_final_damage"]
        skill_normal_damage.value=0
    }
    console.log(dropdown_val)
}
function changeColor(button) {
    // 모든 버튼에서 selected 클래스 제거
    const buttons = document.querySelectorAll('.number-button');

    // 선택된 버튼에만 selected 클래스 추가
    button.classList.add('selected');
}
let formCounter = 0;

function addInputField(){
    formCounter++;
    const newInputBox = document.createElement('div');
    newInputBox.classList.add('input-box');
    newInputBox.innerHTML=`
        <div id="spec-container${formCounter}">
            <label for="input${formCounter}"> 옵션 선택 :</label>
            <select id="option-type${formCounter}" name="option-type${formCounter}" onchange="load_optionform(${formCounter})">
                <option value="none">---select---</option>
                <option value="starforce">스타포스</option>
                <option value="chuu">추옵</option>
            </select>
        </div>
    `;
    document.getElementById('equipment-container').appendChild(newInputBox)
}

function load_optionform(cnt){
    const option_name = document.getElementById("option-type" + cnt.toString()).value
    const existingForm = document.getElementById(`extra-options${cnt}`);
    if (existingForm) {
        existingForm.remove(); // 기존 폼 삭제
    }
    if (option_name === "starforce"){
        const addHTML = `
        <div id="extra-options${cnt}">
            <label>부위:</label>
            <select id="equipment-type${formCounter}" name="equipment-type${formCounter}">
                <option value="none">---select---</option>
                <option value="모자">모자</option>
                <option value="얼굴장식">얼굴장식</option>
                <option value="눈장식">눈장식</option>
                <option value="귀고리">귀고리</option>
                <option value="상의">상의</option>
                <option value="하의">하의</option>
                <option value="신발">신발</option>
                <option value="장갑">장갑</option>
                <option value="망토">망토</option>
                <option value="보조무기">보조무기</option>
                <option value="무기">무기</option>
                <option value="반지1">반지1</option>
                <option value="반지2">반지2</option>
                <option value="반지3">반지3</option>
                <option value="반지4">반지4</option>
                <option value="펜던트1">펜던트1</option>
                <option value="펜던트2">펜던트2</option>
                <option value="벨트">벨트</option>
                <option value="어깨장식">어깨장식</option>
                <option value="포켓 아이템">포켓 아이템</option>
                <option value="기계 심장">기계 심장</option>
            </select>
            <label for="starforce_amt${cnt}">스타포스:</label>
            <input type="text" id="starforce_amt${cnt}" name="starforce_amt${cnt}" placeholder="예: 15">
        </div>
        `;
        document.getElementById('spec-container' + cnt.toString()).insertAdjacentHTML('beforeend', addHTML)
    }
    else if (option_name === "chuu"){
        console.log(cnt + 1)
        // 추가 로직 필요
    }
}

function update_spec(){
    const json_dict = {
        "str" : "STR",
        "str_wo_rate" : "STR(% 미적용)",
        "str_rate" : "STR%",
        "dex" : "DEX",
        "dex_wo_rate" : "DEX(% 미적용)",
        "dex_rate" : "DEX%",
        "int" : "INT",
        "int_wo_rate" : "INT(% 미적용)",
        "int_rate" : "INT%",
        "luk" : "LUK",
        "luk_wo_rate" : "LUK(% 미적용)",
        "luk_rate" : "LUK%",
        "max_hp" : "최대 HP",
        "max_hp_wo_rate" : "최대 HP(% 미적용)",
        "max_hp_rate" : "최대 HP%",
        "attack_power" : "공격력",
        "attack_power_wo_rate" : "공격력(% 미적용)",
        "attack_power_rate" : "공격력%",
        "magic_power" : "마력",
        "magic_power_wo_rate" : "마력(% 미적용)",
        "magic_power_rate" : "마력%",
        "ignore_monster_armor" : "방무(%)",
        "boss_damage" : "보공(%)",
        "damage" : "데미지(%)",
        "normal_damage" : "일몹뎀(%)",
        "critical_rate" : "크확(%)",
        "critical_damage" : "크뎀(%)",
        "final_damage" : "최종뎀(%)",
        "buff" : "벞지(%)",
        "insight" : "내성 무시(%)",
        "starforce" : "스타포스",
        "arcane_force" : "아케인포스",
        "authentic_force" : "어센틱포스"  
    };
    const dopingcheck = document.getElementById('dopingcheck').checked ? 'spec_w_doping' : 'spec_final';
    const storedData = JSON.parse(localStorage.getItem(dopingcheck))
    if(dopingcheck === "spec_w_doping" && storedData === null){
        alert("도핑을 클릭하고 한줄데미지를 먼저 계산해주세요.")
        document.getElementById('dopingcheck').checked = false;
    }
    else{
        const name = document.getElementById('name');
        name.innerHTML = `이름 : ${storedData["name"]}`;
        const container = document.getElementById('data-container');
        container.innerHTML = '';
        for (const key in json_dict){
            const value = storedData[key];
            const itemDiv = document.createElement('div');
            itemDiv.classList.add('item');
            itemDiv.innerHTML = `<strong>${json_dict[key]}:</strong> ${value}`;
            container.appendChild(itemDiv);
        }
        const time = document.getElementById("time");
        time.innerHTML = `최종 업데이트 시간 : ${localStorage.getItem('time')}`
    }
}

update_spec()

function update_map_region(){
    const force_type = document.getElementById('force_type');
    const map_region = document.getElementById('map_region');
    map_region.innerHTML = '';
    if (force_type.value === 'arcane'){
        const options = ['소멸의 여로', '리버스 시티', '츄츄 아일랜드', '얌얌 아일랜드', '레헬른', '아르카나', '모라스', '에스페라', '셀라스', '문브릿지', '고통의 미궁', '리멘'];
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.textContent = option;
            map_region.appendChild(opt);
        })
    }
    else if (force_type.value === 'authentic'){
        const options = ['세르니움', '호텔 아르크스', '오디움', '도원경', '아르테리아', '카르시온', '탈라하트'];
        options.forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.textContent = option;
            map_region.appendChild(opt);
        })
    }
    map_region.disabled = false;
    const map_name = document.getElementById('map_name');
    if(force_type.value === 'arcane'){
    map_name.innerHTML = `<option value="풍화된 기쁨의 땅">풍화된 기쁨의 땅</option>
                        <option value="풍화된 기쁨과 분노의 땅">풍화된 기쁨과 분노의 땅</option>
                        <option value="풍화된 분노의 땅">풍화된 분노의 땅</option>
                        <option value="풍화된 분노와 슬픔의 땅">풍화된 분노와 슬픔의 땅</option>
                        <option value="풍화된 슬픔의 땅">풍화된 슬픔의 땅</option>
                        <option value="풍화된 슬픔과 즐거움의 땅">풍화된 슬픔과 즐거움의 땅</option>
                        <option value="풍화된 즐거움의 땅">풍화된 즐거움의 땅</option>
                        <option value="숨겨진 호숫가">숨겨진 호숫가</option>
                        <option value="암석의 영토">암석의 영토</option>
                        <option value="암석과 화염의 영토">암석과 화염의 영토</option>
                        <option value="화염의 영토">화염의 영토</option>
                        <option value="화염과 영혼의 영토">화염과 영혼의 영토</option>
                        <option value="영혼의 영토">영혼의 영토</option>
                        <option value="숨겨진 화염지대">숨겨진 화염지대</option>
                        <option value="세 갈래길1">세 갈래길1</option>
                        <option value="동굴의 서쪽길1">동굴의 서쪽길1</option>
                        <option value="동굴의 서쪽길2">동굴의 서쪽길2</option>
                        <option value="동굴의 동쪽길1">동굴의 동쪽길1</option>
                        <option value="동굴의 동쪽길2">동굴의 동쪽길2</option>
                        <option value="세 갈래길2">세 갈래길2</option>
                        <option value="동굴 위쪽">동굴 위쪽</option>
                        <option value="동굴 아래쪽">동굴 아래쪽</option>
                        <option value="동굴의 깊숙한 곳">동굴의 깊숙한 곳</option>
                        <option value="아르마의 은신처">아르마의 은신처</option>
                        <option value="숨겨진 동굴">숨겨진 동굴</option>`;
    }
    else if(force_type.value === 'authentic'){
        map_name.innerHTML = `<option value="해변 암석지대 1">해변 암석지대 1</option><option value="해변 암석지대 2">해변 암석지대 2</option><option value="해변 암석지대 3">해변 암석지대 3</option><option value="해변 암석지대 4">해변 암석지대 4</option><option value="세르니움 서쪽 성벽 1">세르니움 서쪽 성벽 1</option><option value="세르니움 서쪽 성벽 2">세르니움 서쪽 성벽 2</option><option value="세르니움 서쪽 성벽 3">세르니움 서쪽 성벽 3</option><option value="왕립 도서관 제1구역">왕립 도서관 제1구역</option><option value="왕립 도서관 제2구역">왕립 도서관 제2구역</option><option value="왕립 도서관 제3구역">왕립 도서관 제3구역</option><option value="왕립 도서관 제4구역">왕립 도서관 제4구역</option><option value="왕립 도서관 제5구역">왕립 도서관 제5구역</option><option value="왕립 도서관 제6구역">왕립 도서관 제6구역</option><option value="세르니움 동쪽 성벽 1">세르니움 동쪽 성벽 1</option><option value="세르니움 동쪽 성벽 2">세르니움 동쪽 성벽 2</option><option value="세르니움 동쪽 성벽 3">세르니움 동쪽 성벽 3</option><option value="불타는 왕립 도서관 제1구역">불타는 왕립 도서관 제1구역</option><option value="불타는 왕립 도서관 제2구역">불타는 왕립 도서관 제2구역</option><option value="불타는 왕립 도서관 제3구역">불타는 왕립 도서관 제3구역</option><option value="불타는 왕립 도서관 제4구역">불타는 왕립 도서관 제4구역</option><option value="불타는 왕립 도서관 제5구역">불타는 왕립 도서관 제5구역</option><option value="불타는 왕립 도서관 제6구역">불타는 왕립 도서관 제6구역</option><option value="격전의 서쪽 성벽 1">격전의 서쪽 성벽 1</option><option value="격전의 서쪽 성벽 2">격전의 서쪽 성벽 2</option><option value="격전의 서쪽 성벽 3">격전의 서쪽 성벽 3</option><option value="격전의 서쪽 성벽 4">격전의 서쪽 성벽 4</option><option value="격전의 동쪽 성벽 1">격전의 동쪽 성벽 1</option><option value="격전의 동쪽 성벽 2">격전의 동쪽 성벽 2</option><option value="격전의 동쪽 성벽 3">격전의 동쪽 성벽 3</option><option value="격전의 동쪽 성벽 4">격전의 동쪽 성벽 4</option><option value="격전의 동쪽 성벽 5">격전의 동쪽 성벽 5</option><option value="격전의 동쪽 성벽 6">격전의 동쪽 성벽 6</option>`;
    }
}

function update_map_name(){
    const map_region = document.getElementById('map_region');
    const map_name = document.getElementById('map_name');
    map_name.innerHTML = '';

    const maps = {
        '소멸의 여로': [
            '풍화된 기쁨의 땅', '풍화된 기쁨과 분노의 땅', '풍화된 분노의 땅', '풍화된 분노와 슬픔의 땅', 
            '풍화된 슬픔의 땅', '풍화된 슬픔과 즐거움의 땅', '풍화된 즐거움의 땅', '숨겨진 호숫가', 
            '암석의 영토', '암석과 화염의 영토', '화염의 영토', '화염과 영혼의 영토', '영혼의 영토', 
            '숨겨진 화염지대', '세 갈래길1', '동굴의 서쪽길1', '동굴의 서쪽길2', '동굴의 동쪽길1', 
            '동굴의 동쪽길2', '세 갈래길2', '동굴 위쪽', '동굴 아래쪽', '동굴의 깊숙한 곳', 
            '아르마의 은신처', '숨겨진 동굴'
        ],
        '리버스 시티': [
            '지하선로1', '지하선로2', '지하선로3', '지하선로4', '지하선로5', '지하선로6', 
            'T-boy의 연구열차1', 'T-boy의 연구열차2', 'T-boy의 연구열차3', '숨겨진 연구열차', 
            '지하열차1', '지하열차2', '지하열차3', '지상열차1', '지상열차2', '지상열차3', 
            '숨겨진 지하열차', 'M타워2', 'M타워3', 'M타워4', '숨겨진 M타워'
        ],
        '츄츄 아일랜드': [
            '폭포 아래', '격류지대 3', '격류지대 2', '격류지대 1', '츄츄빌리지 입구', '동산 입구', 
            '알록달록 숲지대1', '알록달록 숲지대2', '알록달록 숲지대3', '오색동산 깊은 곳', 
            '길쭉 동글숲1', '길쭉 동글숲2', '몽땅 동글숲1', '몽땅 동글숲2', 
            '츄릅포레스트 깊은 곳', '고래산 초입', '고래산 중턱1', '고래산 정상', 
            '고래산 중턱2', '거대한 꼬리'
        ],
        '얌얌 아일랜드': [
            '머쉬버드 숲1', '머쉬버드 숲2', '머쉬버드 숲3', '머쉬버드 숲4', '머쉬버드 숲5', 
            '머쉬버드 숲6', '일리야드 들판1', '일리야드 들판2', '일리야드 들판3', '일리야드 들판4', 
            '일리야드 들판5', '일리야드 들판6', '펑고스 숲1', '펑고스 숲2', '펑고스 숲3', 
            '펑고스 숲4', '펑고스 숲5', '펑고스 숲6', '숨겨진 머쉬버드 숲', 
            '숨겨진 일리야드 들판', '숨겨진 펑고스 숲'
        ],
        '레헬른': [
            '무법자들의 거리1', '무법자들의 거리2', '무법자들의 거리3', '닭이 뛰노는 곳1', 
            '닭이 뛰노는 곳2', '닭이 뛰노는 곳3', '우승 접시의 거리1', '우승 접시의 거리2', 
            '본색을 드러내는 곳1', '본색을 드러내는 곳2', '본색을 드러내는 곳3', 
            '춤추는 구두 점령지1', '춤추는 구두 점령지2', '악몽의 시계탑 1층', 
            '악몽의 시계탑 2층', '악몽의 시계탑 3층', '악몽의 시계탑 4층', 
            '악몽의 시계탑 5층'
        ],
        '아르카나': [
            '물의 숲', '햇살의 숲', '물과 햇살의 숲', '흙의 숲', '햇살과 흙의 숲', 
            '서리구름의 숲', '번개구름의 숲', '서리와 번개의 숲1', '서리와 번개의 숲2', 
            '맹독의 숲', '폭발의 숲', '맹독과 폭발의 숲1', '맹독과 폭발의 숲2', 
            '동굴 윗길', '동굴 윗길 깊은 곳 1', '동굴 윗길 깊은 곳 2', 
            '동굴 윗길 깊디 깊은 곳', '동굴 아랫길', '동굴 아랫길 깊은 곳 1', 
            '동굴 아랫길 깊은 곳 2', '동굴 아랫길 깊디 깊은 곳', 
            '다섯 갈래 동굴', '다섯 갈래 동굴 윗길', '다섯 갈래 동굴 사잇길', 
            '다섯 갈래 동굴 아랫길', '정령의 나무 밑 동굴'
        ],
        '모라스': [
            '산호 숲으로 가는 길2', '산호 숲으로 가는 길3', '산호 숲으로 가는 길4', 
            '도둑고양이 출몰지', '도둑고양이 출몰지2', '형님들 구역', '형님들 구역2', 
            '형님들 구역3', '그림자가 춤추는 곳2', '그림자가 춤추는 곳3', 
            '그림자가 춤추는 곳4', '폐쇄구역', '폐쇄구역2', '폐쇄구역3', 
            '그날의 트뤼에페2', '그날의 트뤼에페3', '그날의 트뤼에페4'
        ],
        '에스페라': [
            '생명이 시작되는 곳2', '생명이 시작되는 곳3', '생명이 시작되는 곳4', 
            '생명이 시작되는 곳5', '생명이 시작되는 곳6', '생명이 시작되는 곳7', 
            '거울빛에 물든 바다2', '거울빛에 물든 바다3', '거울빛에 물든 바다4', 
            '거울빛에 물든 바다5', '거울빛에 물든 바다6', '거울빛에 물든 바다7', 
            '거울에 비친 빛의 신전2', '거울에 비친 빛의 신전3', '거울에 비친 빛의 신전4'
        ],
        '셀라스': [
            '빛이 마지막으로 닿는 곳 1', '빛이 마지막으로 닿는 곳 2', '빛이 마지막으로 닿는 곳 3', 
            '빛이 마지막으로 닿는 곳 4', '빛이 마지막으로 닿는 곳 5', '빛이 마지막으로 닿는 곳 6', 
            '빛이 마지막으로 닿는 곳 7', '빛이 마지막으로 닿는 곳 8', '빛이 마지막으로 닿는 곳 9', 
            '끝없이 추락하는 심해 1', '끝없이 추락하는 심해 2', '끝없이 추락하는 심해 3', 
            '끝없이 추락하는 심해 4', '끝없이 추락하는 심해 5', '끝없이 추락하는 심해 6', 
            '별이 삼켜진 심해 1', '별이 삼켜진 심해 2', '별이 삼켜진 심해 3', 
            '별이 삼켜진 심해 4', '별이 삼켜진 심해 5', '별이 삼켜진 심해 6'
        ],
        '문브릿지': [
            '사상의 경계1', '사상의 경계2', '사상의 경계3', '사상의 경계4', 
            '사상의 경계5', '사상의 경계6', '미지의 안개1', '미지의 안개2', 
            '미지의 안개3', '미지의 안개4', '미지의 안개5', '미지의 안개6', 
            '공허의 파도1', '공허의 파도2', '공허의 파도3', '공허의 파도4', 
            '공허의 파도5', '공허의 파도6'
        ],
        '고통의 미궁': [
            '고통의 미궁 내부1', '고통의 미궁 내부2', '고통의 미궁 내부3', 
            '고통의 미궁 내부4', '고통의 미궁 내부5', '고통의 미궁 내부6', 
            '고통의 미궁 중심부1', '고통의 미궁 중심부2', '고통의 미궁 중심부3', 
            '고통의 미궁 중심부4', '고통의 미궁 중심부5', '고통의 미궁 중심부6', 
            '고통의 미궁 중심부7', '고통의 미궁 최심부1', '고통의 미궁 최심부2', 
            '고통의 미궁 최심부3', '고통의 미궁 최심부4', '고통의 미궁 최심부5', 
            '고통의 미궁 최심부6'
        ],
        '리멘': [
            '세계의 눈물 하단1', '세계의 눈물 하단2', '세계의 눈물 하단3', 
            '세계의 눈물 중단1', '세계의 눈물 중단2', '세계의 눈물 중단3', 
            '세계의 눈물 중단4', '세계가 끝나는 곳 1-4', '세계가 끝나는 곳 1-5', 
            '세계가 끝나는 곳 1-6', '세계가 끝나는 곳 1-7', '세계가 끝나는 곳 1-8', 
            '세계가 끝나는 곳 1-9', '세계가 끝나는 곳 2-2', '세계가 끝나는 곳 2-3', 
            '세계가 끝나는 곳 2-4', '세계가 끝나는 곳 2-5', '세계가 끝나는 곳 2-6', 
            '세계가 끝나는 곳 2-7', '세계가 끝나는 곳 2-8'
        ],
        '세르니움': [
            '해변 암석지대 1', '해변 암석지대 2', '해변 암석지대 3', 
            '해변 암석지대 4', '세르니움 서쪽 성벽 1', '세르니움 서쪽 성벽 2', 
            '세르니움 서쪽 성벽 3', '왕립 도서관 제1구역', '왕립 도서관 제2구역', 
            '왕립 도서관 제3구역', '왕립 도서관 제4구역', '왕립 도서관 제5구역', 
            '왕립 도서관 제6구역', '세르니움 동쪽 성벽 1', '세르니움 동쪽 성벽 2', 
            '세르니움 동쪽 성벽 3', '불타는 왕립 도서관 제1구역', 
            '불타는 왕립 도서관 제2구역', '불타는 왕립 도서관 제3구역', 
            '불타는 왕립 도서관 제4구역', '불타는 왕립 도서관 제5구역', 
            '불타는 왕립 도서관 제6구역', '격전의 서쪽 성벽 1', '격전의 서쪽 성벽 2', 
            '격전의 서쪽 성벽 3', '격전의 서쪽 성벽 4', '격전의 동쪽 성벽 1', 
            '격전의 동쪽 성벽 2', '격전의 동쪽 성벽 3', '격전의 동쪽 성벽 4', 
            '격전의 동쪽 성벽 5', '격전의 동쪽 성벽 6'
        ],
        '호텔 아르크스': [
            '무법자들이 지배하는 황야1', '무법자들이 지배하는 황야2', 
            '무법자들이 지배하는 황야3', '무법자들이 지배하는 황야4', 
            '낭만이 저무는 자동차 극장1', '낭만이 저무는 자동차 극장2', 
            '낭만이 저무는 자동차 극장3', '낭만이 저무는 자동차 극장4', 
            '낭만이 저무는 자동차 극장5', '낭만이 저무는 자동차 극장6', 
            '종착지 없는 횡단열차1', '종착지 없는 횡단열차2', '종착지 없는 횡단열차3', 
            '종착지 없는 횡단열차4', '종착지 없는 횡단열차5', '종착지 없는 횡단열차6'
        ],
        '오디움': [
            '성문으로 가는 길 1', '성문으로 가는 길 2', '성문으로 가는 길 3', 
            '성문으로 가는 길 4', '성문으로 가는 길 5', '점령당한 골목 1', 
            '점령당한 골목 2', '점령당한 골목 3', '점령당한 골목 4', 
            '볕 드는 실험실 1', '볕 드는 실험실 2', '볕 드는 실험실 3', 
            '잠긴 문 뒤 실험실 1', '잠긴 문 뒤 실험실 2', '잠긴 문 뒤 실험실 3', 
            '잠긴 문 뒤 실험실 4'
        ],
        '도원경': [
            '생기가 돌아오는 봄 1', '생기가 돌아오는 봄 2', '생기가 돌아오는 봄 3', 
            '생기가 돌아오는 봄 4', '생기가 돌아오는 봄 5', '빛이 약한 여름 1', 
            '빛이 약한 여름 2', '빛이 약한 여름 3', '빛이 약한 여름 4', 
            '빛이 약한 여름 5', '색깔이 옅은 가을 1', '색깔이 옅은 가을 2', 
            '색깔이 옅은 가을 3', '색깔이 옅은 가을 4', '색깔이 옅은 가을 5', 
            '참혹한 흔적의 겨울 1', '참혹한 흔적의 겨울 2', 
            '참혹한 흔적의 겨울 3', '참혹한 흔적의 겨울 4', 
            '참혹한 흔적의 겨울 5'
        ],
        '아르테리아': [
            '북쪽 외곽지역', '외곽 전투지역 1', '서쪽 외곽지역', 
            '남쪽 외곽지역', '외곽 전투지역 2', '동쪽 외곽지역', 
            '최하층 통로 1', '최하층 통로 2', '최하층 통로 3', 
            '최하층 통로 4', '최하층 통로 5', '최하층 통로 6', 
            '최상층 통로 1', '최상층 통로 2', '최상층 통로 3', 
            '최상층 통로 4', '최상층 통로 5', '최상층 통로 6', 
            '최상층 통로 7', '최상층 통로 8'
        ],
        '카르시온': [
            '거대 산호 군락 1', '거대 산호 군락 2', '거대 산호 군락 3', 
            '잔잔한 해안가 1', '잔잔한 해안가 2', '잔잔한 해안가 3', 
            '휘감기는 숲 1', '휘감기는 숲 2', '휘감기는 숲 3', 
            '어둠이 내리는 나무줄기 1', '어둠이 내리는 나무줄기 2', 
            '어둠이 내리는 나무줄기 3', '숨이 멎어드는 동굴 1', 
            '숨이 멎어드는 동굴 2', '숨이 멎어드는 동굴 3', 
            '숨이 멎어드는 동굴 4', '가라앉은 유적지 1', 
            '가라앉은 유적지 2', '가라앉은 유적지 3', '가라앉은 유적지 4'
        ],
        '탈라하트': [
            '재와 침묵의 땅 1', '재와 침묵의 땅 2', '재와 침묵의 땅 3', 
            '재와 침묵의 땅 4', '재와 침묵의 땅 5', 
            '섭리와 운명의 전쟁터 1', '섭리와 운명의 전쟁터 2', 
            '섭리와 운명의 전쟁터 3', 
            '심판과 운명의 전쟁터 1', '심판과 운명의 전쟁터 2', 
            '심판과 운명의 전쟁터 3', 
            '영원과 운명의 전쟁터 1', '영원과 운명의 전쟁터 2', 
            '영원과 운명의 전쟁터 3', 
            '밤의 길 1', '밤의 길 2', '밤의 길 3', '밤의 길 4', 
            '환영의 길 1', '환영의 길 2', '환영의 길 3', '환영의 길 4'
        ]
    };

    if (maps[map_region.value]) {
        maps[map_region.value].forEach(option => {
            const opt = document.createElement('option');
            opt.value = option;
            opt.textContent = option;
            map_name.appendChild(opt);
        })
    }

    map_name.disabled = false;
}
function toggleButton(button, rowId) {
    const buttons = document.querySelectorAll(`#${rowId} .number-button`);
    
    // 해당 줄의 모든 버튼을 순회하여
    buttons.forEach(btn => {
        if (btn === button) {
            // 선택된 버튼이 이미 활성화되어 있으면 비활성화
            if (btn.classList.contains('selected')) {
                btn.classList.remove('selected');
                btn.style.backgroundColor = '#3498db'; // 기본 색상으로 변경
            } else {
                // 그렇지 않다면 다른 버튼은 비활성화하고, 현재 버튼을 활성화
                buttons.forEach(b => b.classList.remove('selected'));
                btn.classList.add('selected');
                btn.style.backgroundColor = '#2ecc71'; // 선택된 색상으로 변경
            }
        } else {
            btn.classList.remove('selected');
            btn.style.backgroundColor = '#3498db'; // 다른 버튼은 기본 색상으로
        }
    });
}

function submitCharactername(){
    let selectedItems = [];
    const characterName = document.getElementById('nameInput').value;
    console.log(characterName)
    const isChecked = document.getElementById('combatOrders').checked ? 1 : 0;
    if(characterName){
        selectedItems.push(`characterName=${encodeURIComponent(characterName)}`);
    }
    if(isChecked){
        selectedItems.push(`combat_flag=${isChecked}`);
    }

    let selectedPresets = [];

    let selectedPreset1 = document.querySelector('#row1 .number-button.selected')?.textContent || null;
    let selectedPreset2 = document.querySelector('#row2 .number-button.selected')?.textContent || null;
    let selectedPreset3 = document.querySelector('#row3 .number-button.selected')?.textContent || null;
    let selectedPreset4 = document.querySelector('#row4 .number-button.selected')?.textContent || null;
    let selectedPreset5 = document.querySelector('#row5 .number-button.selected')?.textContent || null;

    if (selectedPreset1 !== null) selectedPresets.push(selectedPreset1);
    if (selectedPreset2 !== null) selectedPresets.push(selectedPreset2);
    if (selectedPreset3 !== null) selectedPresets.push(selectedPreset3);
    if (selectedPreset4 !== null) selectedPresets.push(selectedPreset4);
    if (selectedPreset5 !== null) selectedPresets.push(selectedPreset5);
    let queryString = selectedItems.join('&')
    if (selectedPresets.length!==0){
        queryString = queryString + '&' + selectedPresets.map(preset => `presets=${encodeURIComponent(preset)}`).join('&')
    }
    if (characterName){
        fetch(`/initialize/?${queryString}`)
            .then(response => response.json())
            .then(data =>{
                if (data[0].length === 5){
                    if(data[0][4].length === 0){
                        localStorage.setItem('guild_doping', JSON.stringify(data[0][0]))
                        localStorage.setItem('spec_final', JSON.stringify(data[0][1]))
                        localStorage.setItem('yanus_spec', JSON.stringify(data[0][2]))
                        localStorage.setItem('fountain_spec', JSON.stringify(data[0][3]))
                        localStorage.setItem('time', data[1])
                        if(localStorage.getItem("spec_w_doping") !== null){
                            localStorage.removeItem("spec_w_doping");
                            document.getElementById('dopingcheck').checked = false;
                        }
                        alert('데이터 불러오기가 완료되었습니다.')
                        document.getElementById('nameInput').value = "";
                        update_spec()
                        const old = document.getElementById('old');
                        const fd = document.getElementById('fd');
                        old.innerHTML = '';
                        fd.innerHTML = '';
                        update_skill()
                    }
                    else{
                        alert(data[0][4])
                        console.log(data[0][4])
                    }
                }
                else{
                    console.error('expected 3 elements.')
                }
            })
            .catch(error =>{
                console.error('error:', error);
            });
    }
}

function submitForm() {
    if (localStorage.getItem("spec_final") === null){
        alert("스펙을 가져와주세요.")
        return
    }
    // 체크된 항목을 가져옵니다
    const dopings = document.querySelectorAll('input[name="doping"]:checked');
    const skill_damage = document.getElementById('skill_damage').value
    const attack_count = document.getElementById('attack_count').value
    const hyper_damage = document.getElementById('hyper_damage').value
    const core_reinforce = document.getElementById('core_reinforce').value
    const core_ignore_monster_armor = document.getElementById('core_ignore_monster_armor').value
    const skill_ignore_monster_armor = document.getElementById('skill_ignore_monster_armor').value
    const skill_final_damage = document.getElementById('skill_final_damage').value
    const skill_normal_damage = document.getElementById('skill_normal_damage').value
    const force_type = document.getElementById('force_type').value
    const map_region = document.getElementById('map_region').value
    const map_name = document.getElementById('map_name').value
    const specFinal = localStorage.getItem('spec_final');
    const guild_doping = localStorage.getItem('guild_doping');
    let selectedItems = [];
    dopings.forEach((doping) => {
        selectedItems.push(`doping=${encodeURIComponent(doping.value)}`);
    });
    if (skill_damage){
        selectedItems.push(`dmg=${encodeURIComponent(skill_damage)}`);
    }
    if (attack_count){
        selectedItems.push(`attack_count=${encodeURIComponent(attack_count)}`);
    }
    if (hyper_damage){
        selectedItems.push(`hyper_damage=${encodeURIComponent(hyper_damage)}`);
    }
    if(core_reinforce){
        selectedItems.push(`core_reinforce=${encodeURIComponent(core_reinforce)}`);
    }
    if(core_ignore_monster_armor){
        selectedItems.push(`core_igm=${encodeURIComponent(core_ignore_monster_armor)}`);
    }
    if(skill_ignore_monster_armor){
        selectedItems.push(`skill_igm=${encodeURIComponent(skill_ignore_monster_armor)}`);
    }
    if(skill_final_damage){
        selectedItems.push(`skill_final_damage=${encodeURIComponent(skill_final_damage)}`);
    }
    if(skill_normal_damage){
        selectedItems.push(`skill_normal_damage=${encodeURIComponent(skill_normal_damage)}`);
    }
    if(force_type){
        selectedItems.push(`map_type=${encodeURIComponent(force_type)}`);
    }
    if(map_region){
        selectedItems.push(`map_region=${encodeURIComponent(map_region)}`);
    }
    if(map_name){
        selectedItems.push(`map_name=${encodeURIComponent(map_name)}`);
    }
    if(specFinal){
        selectedItems.push(`final=${encodeURIComponent(specFinal)}`);
    }
    if(guild_doping){
        selectedItems.push(`guild_doping=${encodeURIComponent(guild_doping)}`);
    }
    const queryString = selectedItems.join('&');
    // GET 요청을 보냅니다
    fetch(`/calculate/?${queryString}`)
        .then(response => response.json())
        .then(data => {
            // 결과를 HTML에 표시합니다
            const sugong = document.getElementById('sugong');
            const old = document.getElementById('old');
            const fd = document.getElementById('fd');
            const mob_hp = document.getElementById('hp');
            sugong.innerHTML = '';
            old.innerHTML = '';
            fd.innerHTML = '';
            mob_hp.innerHTML = '';
            const p0 = document.createElement('p');
            p0.textContent = data[0].toLocaleString('ko-KR');
            old.appendChild(p0)
            const p1 = document.createElement('p');
            p1.textContent = data[1].toLocaleString('ko-KR');
            fd.appendChild(p1)
            const p2 = document.createElement('p');
            p2.textContent = data[2].toLocaleString('ko-KR');
            mob_hp.appendChild(p2)
            const p4 = document.createElement('p');
            p4.textContent = data[4].toLocaleString('ko-KR');
            sugong.appendChild(p4)

            localStorage.setItem('spec_w_doping', JSON.stringify(data[3]))
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
/* demo.js — the scene loaded by index.html?demo=1.
 *
 * It exists for two reasons: it is what the screenshots are taken of, and it is a
 * worked example of the JSON shape for anyone hand-editing a scene file.
 *
 * It is SAMPLE DATA. The march routes are drawn freehand to show what the tool can
 * do; they are not traced from a source. Verify anything here against sources/
 * before it reaches a slide.
 */
(function (global) {
  'use strict';

  function scene() {
    var s = MS_Store.blankScene();

    s.meta.title = 'The Ridda Wars';
    s.meta.subtitle = '11–12 AH · the columns sent out from Madina';
    s.meta.urduTitle = 'جنگِ ردّہ';
    s.meta.note = 'Sample scene. Routes drawn freehand for demonstration - not traced from a source.';

    MS_Proj.fitBBox(s.view, [30.0, 12.0, 60.0, 40.0]);

    s.factions = [
      { id: 'f1', name: 'Columns from Madina', ur: 'مدینہ سے روانہ دستے', color: '#22B694' },
      { id: 'f2', name: 'Byzantine Rome', ur: 'روم', color: '#DC5844' },
      { id: 'f3', name: 'Sasanian Persia', ur: 'فارس', color: '#9877D6' },
      { id: 'f4', name: 'Tribes in revolt', ur: 'مرتد قبائل', color: '#E7A244' }
    ];

    var o = s.objects;

    function push(obj) { o.push(obj); return obj; }

    // --- step 1: the world as it stood -------------------------------------
    push(MS_Store.newTerritory([[27.5, 41.0], [38.5, 38.5], [39.6, 34.2], [36.2, 29.6], [33.0, 31.0], [27.5, 36.5]],
      { faction: 'f2', label: 'Byzantine Rome', ur: 'سلطنتِ روم', opacity: 0.20, step: 1 }));
    push(MS_Store.newTerritory([[41.5, 38.5], [54.0, 38.5], [59.0, 32.0], [53.0, 27.5], [46.0, 29.5], [42.5, 33.0]],
      { faction: 'f3', label: 'Sasanian Persia', ur: 'سلطنتِ فارس', opacity: 0.20, step: 1 }));
    push(MS_Store.newTerritory([[38.2, 26.6], [41.6, 26.2], [42.2, 20.6], [39.4, 19.8], [37.8, 22.5]],
      { faction: 'f1', label: '', opacity: 0.24, step: 1 }));

    var cities = [
      ['Madina', 'مدینہ', 39.611, 24.471, 'capital', 'left'],
      ['Makkah', 'مکہ', 39.826, 21.423, 'capital', 'left'],
      ['Hajar', 'ہجر', 49.588, 25.383, 'city', 'right'],
      ['Nizwa', 'نزوی', 57.533, 22.933, 'city', 'right'],
      ['Sana', 'صنعاء', 44.207, 15.354, 'city', 'below'],
      ['Damascus', 'دمشق', 36.292, 33.513, 'city', 'left'],
      ['Madain', 'مدائن', 44.581, 33.096, 'city', 'left'],
      ['Dumat al-Jandal', 'دومۃ الجندل', 39.869, 29.812, 'fort', 'left']
    ];
    cities.forEach(function (c) {
      push(MS_Store.newSettlement(c[2], c[3], { name: c[0], ur: c[1], tier: c[4], labelPos: c[5], step: 1 }));
    });

    push(MS_Store.newLabel(44.6, 26.4, { text: 'N A J D', size: 22, step: 1 }));
    push(MS_Store.newLabel(38.6, 20.0, { text: 'H I J A Z', size: 20, step: 1 }));
    push(MS_Store.newLabel(52.5, 18.5, { text: 'THE EMPTY QUARTER', size: 17, step: 1 }));

    // --- step 2: the columns march ----------------------------------------
    push(MS_Store.newArrow([[39.9, 24.4], [41.2, 26.6], [41.4, 27.5]],
      { faction: 'f1', width: 15, step: 2 }));
    push(MS_Store.newArrow([[40.1, 24.2], [43.8, 25.2], [46.9, 24.3]],
      { faction: 'f1', width: 13, step: 2 }));
    push(MS_Store.newArrow([[40.3, 23.9], [45.0, 24.8], [49.2, 25.4]],
      { faction: 'f1', width: 12, dashed: true, step: 2 }));
    push(MS_Store.newArrow([[40.4, 23.6], [48.0, 22.0], [56.9, 22.9]],
      { faction: 'f1', width: 12, dashed: true, step: 2 }));

    push(MS_Store.newArmy(42.7, 29.3, {
      name: 'Khalid ibn al-Walid ؓ', ur: 'خالد بن الولید ؓ',
      faction: 'f1', unit: 'cavalry', strength: '', labelPos: 'right', step: 2
    }));
    push(MS_Store.newArmy(46.3, 22.3, {
      name: 'Ikrima ibn Abi Jahl ؓ', ur: 'عکرمہ بن ابی جہل ؓ',
      faction: 'f1', unit: 'infantry', labelPos: 'below', step: 2
    }));
    push(MS_Store.newArmy(51.0, 26.8, {
      name: 'al-Ala ibn al-Hadrami ؓ', ur: 'العلاء بن الحضرمی ؓ',
      faction: 'f1', unit: 'mixed', labelPos: 'right', step: 2
    }));

    // --- step 3: where it was decided -------------------------------------
    push(MS_Store.newBattle(41.4, 27.7, { name: 'Buzakha', ur: 'بزاخہ', date: '11 AH', labelPos: 'left', step: 3 }));
    push(MS_Store.newBattle(47.3, 24.15, { name: 'Yamama', ur: 'یمامہ', date: '12 AH', labelPos: 'right', step: 3 }));

    s.steps.count = 3;
    s.steps.current = 3;
    return s;
  }

  global.MS_Demo = { scene: scene };
})(window);

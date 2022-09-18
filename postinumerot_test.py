# Kirjoita postinumerot-moduulin testit tähän tiedostoon

from postinumerot import postinum

def test_yksi():
    # yksi = juupajoki
    assert postinum("juupajoki") == "Postinumerot: 35540"

def test_monta():
    # monta = järvenpää
    assert postinum("järvenpää") == "Postinumerot: 04400, 04401, 04410, 04420, 04430, 04431, 04440"

def test_nolla():
    # nolla = pukinmäki
    assert postinum("pukinmäki") == None

def test_smart_post():
    assert postinum("smart post") == "Postinumerot: 00104, 00124, 00134, 00144, 00154, 00164, 00174, 00184, 00204, 00214, 00224, 00234, 00244, 00254, 00264, 00274, 00284, 00304, 00324, 00334, 00354, 00374, 00384, 00394, 00404, 00414, 00424, 00434, 00444, 00504, 00514, 00524, 00534, 00544, 00554, 00564, 00574, 00584, 00594, 00614, 00634, 00644, 00654, 00664, 00684, 00694, 00704, 00714, 00724, 00734, 00744, 00754, 00764, 00774, 00794, 00804, 00814, 00824, 00844, 00874, 00884, 00924, 00934, 00944, 00964, 00974, 00984, 00994, 01154, 01204, 01284, 01304, 01344, 01354, 01364, 01374, 01394, 01404, 01454, 01484, 01494, 01514, 01524, 01534, 01604, 01624, 01644, 01654, 01674, 01684, 01694, 01704, 01714, 01724, 01734, 01744, 01804, 01844, 01904, 02104, 02124, 02134, 02154, 02174, 02184, 02204, 02214, 02234, 02244, 02254, 02264, 02274, 02284, 02304, 02324, 02334, 02344, 02364, 02394, 02404, 02434, 02454, 02464, 02484, 02584, 02604, 02614, 02624, 02634, 02654, 02664, 02684, 02704, 02744, 02754, 02764, 02774, 02784, 02884, 02924, 02944, 03104, 03254, 03304, 03404, 03604, 03854, 04134, 04204, 04224, 04234, 04254, 04264, 04304, 04334, 04344, 04364, 04404, 04414, 04424, 04434, 04444, 04504, 04604, 04624, 05204, 05404, 05464, 05804, 05814, 05824, 05834, 05844, 05904, 06104, 06154, 06404, 06454, 07114, 07174, 07504, 07564, 07804, 07884, 07904, 08104, 08154, 08204, 08354, 09124, 09224, 10214, 10304, 10364, 10424, 10524, 10604, 10654, 10904, 10964, 11104, 11114, 11124, 11134, 11714, 12104, 12244, 12404, 12524, 12544, 12604, 12704, 13104, 13134, 13204, 13214, 13304, 13504, 13604, 13724, 14204, 14304, 14504, 14704, 14814, 15104, 15114, 15144, 15154, 15164, 15204, 15214, 15244, 15304, 15504, 15544, 15554, 15564, 15704, 15814, 15864, 15874, 15884, 15954, 16204, 16304, 16604, 16904, 17134, 17204, 17504, 17804, 18104, 18154, 18304, 19114, 19414, 19654, 19704, 20104, 20204, 20214, 20244, 20254, 20304, 20324, 20364, 20384, 20404, 20464, 20524, 20544, 20614, 20664, 20724, 20734, 20744, 20754, 20764, 20784, 20814, 20884, 20904, 21104, 21114, 21144, 21184, 21204, 21214, 21234, 21244, 21254, 21284, 21354, 21384, 21414, 21424, 21494, 21504, 21534, 21604, 21624, 21874, 22415, 23104, 23144, 23264, 23314, 23504, 23804, 24104, 24264, 24804, 25334, 25394, 25414, 25464, 25504, 25704, 26104, 26204, 26664, 27104, 27234, 27324, 27404, 27434, 27504, 27514, 27804, 28104, 28124, 28134, 28204, 28304, 28364, 28374, 28404, 28434, 28454, 28604, 28614, 28804, 28844, 28904, 29204, 29254, 29604, 29814, 29904, 30104, 30304, 30424, 31304, 31384, 31404, 31504, 31604, 31644, 31704, 31764, 32204, 32444, 32504, 32704, 32804, 33104, 33184, 33204, 33214, 33234, 33274, 33304, 33314, 33344, 33404, 33414, 33474, 33484, 33504, 33534, 33544, 33564, 33584, 33614, 33684, 33714, 33724, 33734, 33804, 33824, 33844, 33854, 33874, 33884, 33904, 33954, 33964, 34154, 34244, 34264, 34304, 34604, 34804, 34874, 35304, 35404, 35604, 35704, 35804, 36114, 36204, 36224, 36244, 36284, 36604, 36914, 37104, 37124, 37144, 37474, 37504, 37554, 37574, 37604, 37634, 37804, 37834, 38104, 38204, 38304, 38424, 38464, 38604, 38704, 38714, 38804, 38954, 39104, 39164, 39204, 39504, 39704, 39824, 39934, 40104, 40204, 40254, 40274, 40324, 40344, 40504, 40524, 40644, 40704, 40744, 40804, 40934, 40954, 41164, 41234, 41334, 41344, 41404, 41524, 41664, 41804, 41904, 42104, 42224, 42304, 42604, 42704, 43104, 43504, 43704, 44104, 44204, 44254, 44284, 44504, 44804, 44884, 45104, 45154, 45164, 45204, 45374, 45614, 45704, 45724, 45744, 45914, 46144, 46804, 46904, 46914, 47404, 48104, 48354, 48404, 48604, 48704, 48914, 49224, 49404, 49414, 49424, 49904, 49934, 50104, 50124, 50134, 50174, 50194, 50504, 50604, 50674, 50974, 51204, 51904, 52104, 52204, 52304, 53104, 53204, 53504, 53554, 53604, 53814, 53854, 53904, 53954, 54104, 54504, 54714, 54804, 54924, 55104, 55124, 55304, 55424, 55804, 56104, 56804, 57104, 57134, 57174, 57204, 57214, 57514, 57714, 58504, 58904, 60104, 60124, 60154, 60204, 60224, 60324, 60514, 60554, 60804, 61104, 61304, 61404, 61504, 61604, 61804, 62104, 62204, 62304, 62374, 62424, 62604, 62664, 62804, 62904, 63104, 63304, 63604, 63614, 63704, 63804, 64104, 64204, 64264, 64304, 65104, 65204, 65234, 65284, 65304, 65324, 65354, 65374, 65384, 65414, 65614, 66104, 66144, 66204, 66274, 66304, 66404, 66444, 66504, 66514, 66534, 66604, 66644, 66804, 66854, 66904, 67104, 67204, 67304, 67404, 67604, 67704, 67904, 68104, 68234, 68304, 68374, 68414, 68504, 68554, 68574, 68604, 68624, 68664, 68704, 68824, 68874, 68914, 69104, 69154, 69304, 69604, 69704, 69954, 70104, 70114, 70154, 70204, 70214, 70304, 70344, 70424, 70464, 70504, 70604, 70624, 70704, 70784, 70804, 70824, 70844, 70914, 71164, 71204, 71474, 71754, 71804, 72104, 72304, 72404, 72604, 73104, 73134, 73204, 73304, 73464, 73504, 73604, 73904, 74104, 74124, 74134, 74204, 74304, 74704, 75504, 75534, 75704, 76104, 76154, 76854, 77434, 77604, 77704, 78204, 78214, 78254, 78304, 79104, 79484, 79604, 79704, 80104, 80114, 80144, 80164, 80224, 80264, 80334, 80404, 80714, 80774, 81104, 81204, 81284, 81704, 82204, 82504, 82604, 82734, 82904, 83504, 83704, 83904, 84104, 85104, 85204, 85504, 85804, 85904, 86104, 86304, 86404, 86604, 86714, 86804, 87104, 87204, 87254, 87404, 87504, 87704, 88274, 88304, 88474, 88604, 88614, 88904, 89204, 89404, 90104, 90124, 90134, 90144, 90154, 90234, 90244, 90254, 90404, 90414, 90424, 90444, 90454, 90464, 90504, 90514, 90524, 90534, 90544, 90574, 90584, 90594, 90604, 90624, 90634, 90654, 90674, 90804, 90824, 90834, 90844, 90904, 90944, 91104, 91204, 91304, 91414, 91504, 91604, 91704, 91804, 91904, 92104, 92134, 92144, 92404, 92434, 92704, 92934, 93104, 93144, 93604, 93834, 94104, 94604, 94704, 95164, 95204, 95404, 95424, 95604, 95704, 95904, 95974, 96104, 96204, 96304, 96324, 96404, 96444, 96464, 96904, 96914, 97144, 97224, 97704, 97904, 98104, 98534, 98714, 98904, 99104, 99134, 99304, 99604, 99804, 99834, 99874, 99944, 99954, 99994"

def test_smartpost():
    assert postinum("smartpost") == "Postinumerot: 00104, 00124, 00134, 00144, 00154, 00164, 00174, 00184, 00204, 00214, 00224, 00234, 00244, 00254, 00264, 00274, 00284, 00304, 00324, 00334, 00354, 00374, 00384, 00394, 00404, 00414, 00424, 00434, 00444, 00504, 00514, 00524, 00534, 00544, 00554, 00564, 00574, 00584, 00594, 00614, 00634, 00644, 00654, 00664, 00684, 00694, 00704, 00714, 00724, 00734, 00744, 00754, 00764, 00774, 00794, 00804, 00814, 00824, 00844, 00874, 00884, 00924, 00934, 00944, 00964, 00974, 00984, 00994, 01154, 01204, 01284, 01304, 01344, 01354, 01364, 01374, 01394, 01404, 01454, 01484, 01494, 01514, 01524, 01534, 01604, 01624, 01644, 01654, 01674, 01684, 01694, 01704, 01714, 01724, 01734, 01744, 01804, 01844, 01904, 02104, 02124, 02134, 02154, 02174, 02184, 02204, 02214, 02234, 02244, 02254, 02264, 02274, 02284, 02304, 02324, 02334, 02344, 02364, 02394, 02404, 02434, 02454, 02464, 02484, 02584, 02604, 02614, 02624, 02634, 02654, 02664, 02684, 02704, 02744, 02754, 02764, 02774, 02784, 02884, 02924, 02944, 03104, 03254, 03304, 03404, 03604, 03854, 04134, 04204, 04224, 04234, 04254, 04264, 04304, 04334, 04344, 04364, 04404, 04414, 04424, 04434, 04444, 04504, 04604, 04624, 05204, 05404, 05464, 05804, 05814, 05824, 05834, 05844, 05904, 06104, 06154, 06404, 06454, 07114, 07174, 07504, 07564, 07804, 07884, 07904, 08104, 08154, 08204, 08354, 09124, 09224, 10214, 10304, 10364, 10424, 10524, 10604, 10654, 10904, 10964, 11104, 11114, 11124, 11134, 11714, 12104, 12244, 12404, 12524, 12544, 12604, 12704, 13104, 13134, 13204, 13214, 13304, 13504, 13604, 13724, 14204, 14304, 14504, 14704, 14814, 15104, 15114, 15144, 15154, 15164, 15204, 15214, 15244, 15304, 15504, 15544, 15554, 15564, 15704, 15814, 15864, 15874, 15884, 15954, 16204, 16304, 16604, 16904, 17134, 17204, 17504, 17804, 18104, 18154, 18304, 19114, 19414, 19654, 19704, 20104, 20204, 20214, 20244, 20254, 20304, 20324, 20364, 20384, 20404, 20464, 20524, 20544, 20614, 20664, 20724, 20734, 20744, 20754, 20764, 20784, 20814, 20884, 20904, 21104, 21114, 21144, 21184, 21204, 21214, 21234, 21244, 21254, 21284, 21354, 21384, 21414, 21424, 21494, 21504, 21534, 21604, 21624, 21874, 22415, 23104, 23144, 23264, 23314, 23504, 23804, 24104, 24264, 24804, 25334, 25394, 25414, 25464, 25504, 25704, 26104, 26204, 26664, 27104, 27234, 27324, 27404, 27434, 27504, 27514, 27804, 28104, 28124, 28134, 28204, 28304, 28364, 28374, 28404, 28434, 28454, 28604, 28614, 28804, 28844, 28904, 29204, 29254, 29604, 29814, 29904, 30104, 30304, 30424, 31304, 31384, 31404, 31504, 31604, 31644, 31704, 31764, 32204, 32444, 32504, 32704, 32804, 33104, 33184, 33204, 33214, 33234, 33274, 33304, 33314, 33344, 33404, 33414, 33474, 33484, 33504, 33534, 33544, 33564, 33584, 33614, 33684, 33714, 33724, 33734, 33804, 33824, 33844, 33854, 33874, 33884, 33904, 33954, 33964, 34154, 34244, 34264, 34304, 34604, 34804, 34874, 35304, 35404, 35604, 35704, 35804, 36114, 36204, 36224, 36244, 36284, 36604, 36914, 37104, 37124, 37144, 37474, 37504, 37554, 37574, 37604, 37634, 37804, 37834, 38104, 38204, 38304, 38424, 38464, 38604, 38704, 38714, 38804, 38954, 39104, 39164, 39204, 39504, 39704, 39824, 39934, 40104, 40204, 40254, 40274, 40324, 40344, 40504, 40524, 40644, 40704, 40744, 40804, 40934, 40954, 41164, 41234, 41334, 41344, 41404, 41524, 41664, 41804, 41904, 42104, 42224, 42304, 42604, 42704, 43104, 43504, 43704, 44104, 44204, 44254, 44284, 44504, 44804, 44884, 45104, 45154, 45164, 45204, 45374, 45614, 45704, 45724, 45744, 45914, 46144, 46804, 46904, 46914, 47404, 48104, 48354, 48404, 48604, 48704, 48914, 49224, 49404, 49414, 49424, 49904, 49934, 50104, 50124, 50134, 50174, 50194, 50504, 50604, 50674, 50974, 51204, 51904, 52104, 52204, 52304, 53104, 53204, 53504, 53554, 53604, 53814, 53854, 53904, 53954, 54104, 54504, 54714, 54804, 54924, 55104, 55124, 55304, 55424, 55804, 56104, 56804, 57104, 57134, 57174, 57204, 57214, 57514, 57714, 58504, 58904, 60104, 60124, 60154, 60204, 60224, 60324, 60514, 60554, 60804, 61104, 61304, 61404, 61504, 61604, 61804, 62104, 62204, 62304, 62374, 62424, 62604, 62664, 62804, 62904, 63104, 63304, 63604, 63614, 63704, 63804, 64104, 64204, 64264, 64304, 65104, 65204, 65234, 65284, 65304, 65324, 65354, 65374, 65384, 65414, 65614, 66104, 66144, 66204, 66274, 66304, 66404, 66444, 66504, 66514, 66534, 66604, 66644, 66804, 66854, 66904, 67104, 67204, 67304, 67404, 67604, 67704, 67904, 68104, 68234, 68304, 68374, 68414, 68504, 68554, 68574, 68604, 68624, 68664, 68704, 68824, 68874, 68914, 69104, 69154, 69304, 69604, 69704, 69954, 70104, 70114, 70154, 70204, 70214, 70304, 70344, 70424, 70464, 70504, 70604, 70624, 70704, 70784, 70804, 70824, 70844, 70914, 71164, 71204, 71474, 71754, 71804, 72104, 72304, 72404, 72604, 73104, 73134, 73204, 73304, 73464, 73504, 73604, 73904, 74104, 74124, 74134, 74204, 74304, 74704, 75504, 75534, 75704, 76104, 76154, 76854, 77434, 77604, 77704, 78204, 78214, 78254, 78304, 79104, 79484, 79604, 79704, 80104, 80114, 80144, 80164, 80224, 80264, 80334, 80404, 80714, 80774, 81104, 81204, 81284, 81704, 82204, 82504, 82604, 82734, 82904, 83504, 83704, 83904, 84104, 85104, 85204, 85504, 85804, 85904, 86104, 86304, 86404, 86604, 86714, 86804, 87104, 87204, 87254, 87404, 87504, 87704, 88274, 88304, 88474, 88604, 88614, 88904, 89204, 89404, 90104, 90124, 90134, 90144, 90154, 90234, 90244, 90254, 90404, 90414, 90424, 90444, 90454, 90464, 90504, 90514, 90524, 90534, 90544, 90574, 90584, 90594, 90604, 90624, 90634, 90654, 90674, 90804, 90824, 90834, 90844, 90904, 90944, 91104, 91204, 91304, 91414, 91504, 91604, 91704, 91804, 91904, 92104, 92134, 92144, 92404, 92434, 92704, 92934, 93104, 93144, 93604, 93834, 94104, 94604, 94704, 95164, 95204, 95404, 95424, 95604, 95704, 95904, 95974, 96104, 96204, 96304, 96324, 96404, 96444, 96464, 96904, 96914, 97144, 97224, 97704, 97904, 98104, 98534, 98714, 98904, 99104, 99134, 99304, 99604, 99804, 99834, 99874, 99944, 99954, 99994"
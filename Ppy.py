import streamlit as st
import hashlib
import time

# 1. إعدادات الهوية البصرية الرسمية لمنصة ARK
st.set_page_config(
    page_title="ARK NDT | المنصة التعليمية العالمية للاختبارات غير التدميرية",
    page_icon="🛡️",
    layout="wide"
)

# واجهة التصميم الأنيقة المخصصة لمنصة ARK (تأثير منصة علا - راقٍ وجاذب)
st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: bold; color: #1B365D; text-align: center; font-family: 'Segoe UI', sans-serif; }
    .subtitle { font-size: 19px; color: #7F8C8D; text-align: center; margin-bottom: 35px; }
    .ark-badge { background-color: #27AE60; color: white; padding: 6px 14px; border-radius: 20px; font-weight: bold; font-size: 12px; }
    .course-card { border: 1px solid #BDC3C7; padding: 25px; border-radius: 12px; background-color: #F8F9FA; box-shadow: 0 4px 6px rgba(0,0,0,0.05); margin-bottom: 25px; }
    .source-box { background-color: #EBFAFA; border-left: 6px solid #16A085; padding: 18px; border-radius: 5px; font-family: 'Courier New', monospace; }
    </style>
""", unsafe_allow_html=True)

# 2. الهندسة الأمنية وتشفير البيانات (Cryptography Core)
def make_secure_hash(password: str) -> str:
    """توليد هيدر مشفر لكلمة المرور باستخدام التشفير الرياضي المعقد لمنع الاختراق"""
    salt = "ARK_NDT_SECURE_SALT_2026!!" # الملح البرمجي السري لمنع التخمين
    db_string = password + salt
    return hashlib.sha256(db_string.encode('utf-8')).hexdigest()

# قاعدة بيانات حسابات الطلاب المدفوعة والمشفرة مسبقاً (مستقبلًا ترتبط بـ PostgreSQL / Firebase)
# كلمة المرور الفعلية للحساب التجريبي هي: premium2026
PRE_HASHED_DB = {
    "admin": "3046fbc9086ef8df9671d2b1f8eb3595ca18df88319e7bbd747d25e01f661a3f" 
}

# إدارة بيئة الجلسة الآمنة (Secure Session Management)
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "is_premium" not in st.session_state:
    st.session_state.is_premium = False
if "language" not in st.session_state:
    st.session_state.language = "ar"

# 3. المادة العلمية الموثقة دولياً لـ ARK Core
COURSE_DATA = {
    "ar": {
        "welcome": "🏛️ منصة ARK العالمية لاختبارات NDT",
        "login_header": "🔒 بوابة الاشتراك الآمنة والمشفرة",
        "intro_text": "المرجع الهندسي الأقوى لـ Level 2 - محاضرات متحركة، محاكاة حقلية، ومراجع كود ASME المحدثة.",
        "locked_msg": "⛔ المحتوى محمي بتشفير قوي ومخصص للمشتركين فقط. يرجى تسجيل الدخول أو إدخال كود التفعيل النشط للوصول للمحاضرات.",
        "tabs": ["📺 فيديو الأنميشن والتفسير", "📖 الدليل الفني والمصادر", "🛠️ الحالات الحقلية والمشاكل", "📝 اختبار محاكاة ASNT"],
        "methods": {
            "PT": {
                "title": "المادة (1): اختبار السوائل النافذة (Penetrant Testing - Level 2)",
                "video_desc": "🎬 **مواصفات فيديو الأنميشن التفصيلي:** يعرض المشهد حركة جزيئات الصبغة الحمراء وهي تتغلغل داخل شق مجهري بفعل الخاصية الشعيرية، متبوعاً بنموذج ثلاثي الأبعاد لعمل المظهر (Developer) وهو يسحب الصبغة للخارج (Bleed-out).",
                "manual": "### 📜 الشرح الهندسي الدقيق:\nيعتمد هذا الفحص على **قانون جوران (Jurin's Law)** للخاصية الشعيرية:\n$$\nh = \\frac{2\\gamma \\cos\\theta}{\\rho g r}\n$$\nحيث يتم التحكم في التوتر السطحي وزاوية التلامس كيميائياً لضمان البلل الأقصى (Wettability).",
                "field": "💡 **حالة موقعية:** إذا واجهت مؤشرات كاذبة (False Indications) بسبب خشونة السطح، يشترط كود **ASME Sec V Art. 6** إعادة التنظيف والمسح باستخدام قطعة قماش خالية من الوبر مرطبة بالمذيب، وتجنب الرش المباشر.",
                "sources": "📚 **المصادر الموثقة لهذه المادة:** ASME Section V Article 6 | ISO 3452-1 | ASNT Study Guide."
            },
            "UT": {
                "title": "المادة (2): اختبار الموجات فوق الصوتية (Ultrasonic Testing - Level 2)",
                "video_desc": "🎬 **مواصفات فيديو الأنميشن التفصيلي:** محاكاة ثلاثية الأبعاد للموجات الصوتية عالية التردد (2.25 - 5 MHz) وهي تنكسر داخل حذاء المسبار الزاوي وتنعكس من عيب لحام داخلي لتظهر كإشارة سعة (Amplitude) على شاشة A-scan.",
                "manual": "### 📜 الشرح الهندسي الدقيق:\nيخضع انكسار الموجات الصوتية في المعادن لـ **قانون سنيل (Snell's Law)**:\n$$\n\\frac{\\sin\\theta_1}{v_1} = \\frac{\\sin\\theta_2}{v_2}\n$$\nيتم تقييم حجم العيوب برسم منحنيات تصحيح المسافة والارتفاع (DAC Curve).",
                "field": "💡 **حالة موقعية:** عند الفقدان المفاجئ لنبضة السطح السفلي (Loss of Backwall Echo)، فإن كود **ASME Sec V Art. 4** يوجه الفاحص للتحقق فوراً من وجود انفصال طبقي (Lamination) أو جفاف مادة التلامس (Couplant).",
                "sources": "📚 **المصادر الموثقة لهذه المادة:** ASME Section V Article 4 | AWS D1.1 | ISO 17640."
            }
        }
    },
    "en": {
        "welcome": "🏛️ ARK NDT Global Learning Platform",
        "login_header": "🔒 Secure Encrypted Gateway",
        "intro_text": "The Definitive Level 2 Reference - Masterclasses, Field Simulators, and Verified ASME Code Sources.",
        "locked_msg": "⛔ Content is cryptographically locked. Premium subscription account or active license token required.",
        "tabs": ["📺 Animation Video & Script", "📖 Technical Manual & Sources", "🛠️ Field Troubleshooting", "📝 ASNT Simulator Quiz"],
        "methods": {
            "PT": {
                "title": "Module (1): Liquid Penetrant Testing (PT Level 2)",
                "video_desc": "🎬 **Animation Specification:** High-fidelity 3D rendering of red dye molecules penetrating a surface-breaking micro-crack via capillary force, followed by reverse-capillary blotting action induced by the white developer.",
                "manual": "### 📜 Technical Engineering Discourse:\nThis examination methodology is mathematically governed by **Jurin's Law** for capillary physics:\n$$\nh = \\frac{2\\gamma \\cos\\theta}{\\rho g r}\n$$\nCommercial penetrants are synthesized to maintain a contact angle ($\\theta$) approaching zero to maximize surface wettability.",
                "field": "💡 **Field Case:** When encountering false indications from extreme surface roughness, **ASME Sec V Article 6** mandates re-cleaning and wiping with a lint-free cloth moistened with solvent; direct spraying onto the part is strictly prohibited.",
                "sources": "📚 **Verified Source Documentation:** ASME Section V Article 6 | ISO 3452-1 | ASNT Classroom Training Handbook."
            },
            "UT": {
                "title": "Module (2): Ultrasonic Testing (UT Level 2)",
                "video_desc": "🎬 **Animation Specification:** A dynamic 3D simulator demonstrating high-frequency acoustic wave propagation (2.25 - 5 MHz) refracting through a wedge into a weldment, tracking reflection amplitude signals on a live A-scan chart.",
                "manual": "### 📜 Technical Engineering Discourse:\nAcoustic shear and longitudinal wave refraction across differing material velocities is governed by **Snell's Law**:\n$$\n\\frac{\\sin\\theta_1}{v_1} = \\frac{\\sin\\theta_2}{v_2}\n$$\nDefect sizing is calculated using Distance Amplitude Correction (DAC) curves.",
                "field": "💡 **Field Case:** A sudden loss of the backwall echo signal requires an immediate investigation per **ASME Sec V Article 4** to check for localized acoustic attenuation, couplant failure, or internal planar laminations.",
                "sources": "📚 **Verified Source Documentation:** ASME Section V Article 4 | AWS D1.1 | ISO 17640."
            }
        }
    }
}

# 4. واجهة شريط الأمان والتحكم الجانبي للبرنامج
with st.sidebar:
    st.markdown("## 🛡️ ARK Cyber Security")
    if st.button("🔄 Switch Language (تغيير اللغة)"):
        st.session_state.language = "en" if st.session_state.language == "ar" else "ar"
    
    lang = st.session_state.language
    labels = COURSE_DATA[lang]
    
    st.markdown("---")
    st.markdown(f"### {labels['login_header']}")
    
    user_input = st.text_input("اسم المستخدم / Username")
    pass_input = st.text_input("كلمة المرور / Password", type="password")
    
    if st.button("🔐 التحقق الآمن من التشفير"):
        # حماية ضد هجمات الـ Brute Force بتأخير المعالجة في حال الخطأ
        user_hash = make_secure_hash(pass_input)
        
        if user_input in PRE_HASHED_DB and PRE_HASHED_DB[user_input] == user_hash:
            st.session_state.logged_in = True
            st.session_state.is_premium = True
            st.success("🔓 تم فك تشفير الجلسة وتفعيل حساب ARK Premium!")
            time.sleep(0.5)
            st.rerun()
        else:
            time.sleep(1.5) # خنق برمجى لهجمات التخمين (Rate Limiting)
            st.error("❌ فشل التحقق الآمن. كلمة المرور خاطئة أو الحساب غير نشط.")
            
    if st.session_state.is_premium:
        st.markdown("<span class='ark-badge'>🛡️ SECURE SESSION ACTIVE</span>", unsafe_allow_html=True)

# 5. عرض محتوى الواجهة الرئيسية لمنصة ARK العالمية
st.markdown(f"<div class='main-title'>{labels['welcome']}</div>", unsafe_allow_html=True)
st.markdown(f"<div class='subtitle'>{labels['intro_text']}</div>", unsafe_allow_html=True)

selected_method = st.selectbox("📚 اختر المادة الدراسية / Select Course Module", options=["PT", "UT"])
data = labels["methods"][selected_method]

st.markdown(f"<div class='course-card'><h2>{data['title']}</h2></div>", unsafe_allow_html=True)

# التحقق من صلاحية الجلسة المفتوحة (Access Control Validation)
if not st.session_state.is_premium:
    st.markdown(f"<div style='color: #C0392B; font-weight: bold;'>{labels['locked_msg']}</div>", unsafe_allow_html=True)
    st.info("💡 لفتح المحتوى وتجربة التشفير السيبراني، استخدم حساب الأدمن الآمن: Username: admin | Password: premium2026")
else:
    t1, t2, t3, t4 = st.tabs(labels["tabs"])
    
    with t1:
        st.markdown("### 📺 خطة التحريك الموجهة للمصممين (Animation Spec)")
        st.info(data["video_desc"])
        
    with t2:
        st.markdown(data["manual"])
        st.markdown(f"<div class='source-box'>{data['sources']}</div>", unsafe_allow_html=True)
        
    with t3:
        st.markdown("### 🛠️ دليل الحالات الحقلية المعقدة (Troubleshooting)")
        st.warning(data["field"])
        
    with t4:
        st.markdown("### 📝 اختبارات الكفاءة الموثقة")
        if selected_method == "PT":
            q = st.radio("ما هي زاوية التلامس المثالية للسوائل النافذة الاحترافية؟ / Ideal contact angle?", ["Approaching Zero", "90 Degrees", "180 Degrees"])
            if st.button("إرسال الإجابة / Submit"):
                if q == "Approaching Zero":
                    st.success("🎯 إجابة صحيحة هندسياً ومطابقة لكود ASME!")
                else:
                    st.error("❌ إجابة خاطئة، يرجى مراجعة قانون جوران في تبويب المراجع.")

# 6. لوحة التطوير والتحديث المستقبلي للمنتديات وغرف النقاش
st.markdown("---")
with st.expander("🛠️ ARK Scalability Framework (غرف النقاشات والتطوير المستقبلي)"):
    st.markdown("""
    * **قاعدة البيانات الآمنة (Secure DB):** عند إطلاق المنصة تجارياً، يتم استبدال قاموس الـ `PRE_HASHED_DB` بقاعدة بيانات مشفرة برمجياً عبر الويب (مثل PostgreSQL) لحفظ بيانات آلاف المشتركين بشكل سحابي محمي.
    * **غرف نقاشات الطلاب المشتركة:** يمكن إضافة بند `st.chat_input()` داخل التبويبات وربطه بجداول المحادثات للسماح للطلبة بترك أسئلتهم للمهندس المحاضر ومناقشة تقارير المواقع الهندسية بشكل مباشر.
    """)

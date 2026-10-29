"""
QueryBee - GMIU College Help Chatbot (Rule-Based)
-------------------------------------------------
Topic   : Gyanmanjari Innovative University (GMIU), Bhavnagar
Author  : Rathod Harsh P.  |  Enrollment No: 241105060106
Course  : Diploma IT       |  Subject: AI

How it works:
  1. The user's message is converted to lowercase.
  2. The bot looks for KEYWORDS in the message using if / elif / else rules.
  3. The first rule that matches returns a predefined answer.
  4. If nothing matches, the bot shows a helpful fallback message.

Run in terminal :  python chatbot.py
Run as website  :  streamlit run app.py
"""

import re

BOT_NAME = "QueryBee"

# ---------------------------------------------------------------------------
# Official contact details (source: https://gmiu.edu.in/)
# ---------------------------------------------------------------------------
PHONE = "+91 90999 51160"
ADMISSION_PHONE = "+91 75749 49494"
EMAIL = "info@gmiu.edu.in"
ADDRESS = "Sidsar Road, Bhavnagar, Gujarat 364060"
WEBSITE = "https://gmiu.edu.in/"

WELCOME = (
    "Hello! I am QueryBee, the GMIU College Help Chatbot.\n"
    "I can help you with: About GMIU, Courses, Admission, Eligibility, "
    "Documents, Fees, Scholarships, Hostel, Transport, Placements, "
    "Library, Exams, Facilities and Contact details.\n"
    "Type your question, or type 'help' to see all topics."
)

HELP_TEXT = (
    "You can ask me about:\n"
    "• About GMIU - 'tell me about the university'\n"
    "• Institutes - 'which institutes are there?'\n"
    "• Courses - 'diploma courses', 'BCA', 'B.Pharm', 'MCA'\n"
    "• Admission - 'how to apply?', 'admission process'\n"
    "• Eligibility - 'BTech eligibility', 'BCA eligibility'\n"
    "• Documents - 'documents required'\n"
    "• Fees - 'what are the fees?'\n"
    "• Scholarships - 'scholarship', 'MYSY', 'TFWS'\n"
    "• Hostel - 'hostel facility'\n"
    "• Transport - 'bus facility'\n"
    "• Placement - 'placement statistics'\n"
    "• Library, Exams, Attendance, Timings, Facilities\n"
    "• Contact - 'phone number', 'address', 'email'"
)

FALLBACK = (
    "Sorry, I did not understand that. I am a rule-based bot, so please try "
    "simple keywords like: admission, courses, fees, hostel, placement, "
    "scholarship, library or contact.\n"
    "Type 'help' to see everything I can answer."
)


def has(text, *keywords):
    """Return True if ANY keyword/phrase appears as a whole word in text.
    Whole-word matching stops 'hi' from matching inside 'this' or 'which'."""
    for word in keywords:
        if re.search(r"\b" + re.escape(word) + r"\b", text):
            return True
    return False


def get_response(user_input):
    """Main rule engine: takes the user's message, returns the bot's answer."""
    text = user_input.lower().strip()
    text = re.sub(r"[^a-z0-9+&.\s]", " ", text)   # remove punctuation
    text = re.sub(r"\s+", " ", text).strip()

    # ---------------- 0. Empty input ----------------
    if text == "":
        return "Please type a question so I can help you."

    # ---------------- 1. Greetings & small talk ----------------
    elif len(text.split()) <= 4 and has(text, "hi", "hello", "hey", "hii",
                                        "namaste", "good morning",
                                        "good afternoon", "good evening"):
        return ("Hello! Welcome to QueryBee, the GMIU College Help Chatbot. "
                "How can I help you today?")

    elif has(text, "how are you"):
        return "I am doing great, thank you! How can I help you with GMIU?"

    elif has(text, "who are you", "your name", "what are you", "who made you",
             "who created you", "developer"):
        return ("I am QueryBee, a rule-based chatbot built in Python (if-else "
                "conditions) by Rathod Harsh P. to answer questions about "
                "Gyanmanjari Innovative University (GMIU), Bhavnagar.")

    elif has(text, "help", "menu", "topics", "what can you do", "options"):
        return HELP_TEXT

    elif len(text.split()) <= 5 and has(text, "thanks", "thank you", "thankyou",
                                        "thx"):
        return "You're welcome! Ask me anything else about GMIU."

    elif len(text.split()) <= 4 and has(text, "bye", "goodbye", "exit", "quit",
                                        "see you"):
        return "Goodbye! Best of luck with your studies. Have a great day!"

    # ---------------- 2. Specific topics (most specific rules first) ------
    elif has(text, "hostel", "hostels", "accommodation", "boys hostel",
             "girls hostel"):
        return ("GMIU has separate hostels for boys and girls.\n"
                "• Boys Hostel: near PM Awas, Hillpark Chokadi, Bhavnagar\n"
                "• Girls Hostel: near Gyanmanjari School, Kaliyabid, Bhavnagar\n"
                "• Rooms are spacious and well ventilated (5-6 students per room)\n"
                "• CCTV surveillance for student safety\n"
                f"Hostel enquiry: {ADMISSION_PHONE} / {PHONE}\n"
                "Hostel fee structure: "
                "https://gmiu.edu.in/gmiu/website/admission/transportation.php")

    elif has(text, "bus", "transport", "transportation", "travel", "gps",
             "pickup", "pick up"):
        return ("GMIU runs its own fleet of 11+ modern buses with GPS tracking, "
                "connecting the campus with many points of Bhavnagar city at "
                "nominal fares. Timings are adjusted during exam periods.\n"
                "Transport contact: Mr. Prakashbhai +91 98253 32734")

    elif has(text, "scholarship", "scholarships", "mysy", "freeship",
             "free ship", "tfws", "financial aid", "loan", "emi",
             "digital gujarat"):
        return ("Scholarships & financial help at GMIU (as per the university FAQ):\n"
                "• MYSY (CM Yuva Swavalamban Yojana): for students with 80 PR or "
                "more in Class 10 and family income up to Rs. 6,00,000 - 50% of "
                "tuition fee or Rs. 50,000, whichever is less\n"
                "• SC/ST students (family income up to Rs. 2,50,000): 100% tuition "
                "fee scholarship (Freeship card)\n"
                "• NT/DNT students (family income up to Rs. 2,00,000): "
                "Rs. 50,000 per year\n"
                "• TFWS (Tuition Fee Waiver Scheme): family income below "
                "Rs. 6,00,000, 5% seats, merit based\n"
                "• Help is provided for Freeship Card, Digital Gujarat and MYSY\n"
                "Rules can change every year, so please confirm at: "
                "https://gmiu.edu.in/gmiu/website/admission/scholarships.php")

    elif has(text, "fee", "fees", "tuition", "cost", "price", "charges",
             "payment", "how much"):
        return ("Fees depend on the course and institute, and exact amounts are "
                "not published on the main website.\n"
                "• For Diploma Engineering, the fee is the SAME for Management "
                "Quota and ACPC quota\n"
                "• Hostel fee structure is in the hostel leaflet on the website\n"
                "• Scholarships can reduce the fee - type 'scholarship'\n"
                f"For the exact fee of your course, call {ADMISSION_PHONE} or "
                f"email {EMAIL}.")

    elif has(text, "document", "documents", "certificate", "certificates",
             "papers", "required documents"):
        return ("Documents generally required for admission:\n"
                "• Passport size photos\n"
                "• Class 10 and Class 12 mark sheets\n"
                "• School Leaving / Migration Certificate\n"
                "• Aadhaar card of student and parent\n"
                "• Caste certificate (SC/ST/OBC/SEBC) and Non-creamy layer / EWS "
                "certificate, if applicable\n"
                "• Income certificate\n"
                "• Freeship card (SC/ST), Disability certificate - if applicable\n"
                "• PG students: degree certificate and all graduation mark sheets\n"
                "Providing false documents may lead to cancellation of admission.")

    elif has(text, "eligibility", "eligible", "criteria", "qualification",
             "minimum marks", "percentage", "who can apply"):
        if has(text, "btech", "b tech", "engineering", "degree engineering"):
            return ("B.E./B.Tech eligibility: Class 12 pass in Science stream "
                    "(PCMB) or equivalent from a recognised board. A student with "
                    "a supplementary in 10+2 can apply but must pass before "
                    "admission. Students from any state of India can apply.")
        elif has(text, "bca"):
            return ("BCA eligibility: 10+2 pass in any stream with English as a "
                    "subject, with minimum 45% marks in aggregate (as per UGC rule).")
        elif has(text, "pharm", "pharmacy", "b pharm", "bpharm"):
            return ("B.Pharm eligibility: 10+2 with Physics, Chemistry and "
                    "Biology/Biotechnology/Mathematics - minimum 45% (General) or "
                    "40% (SC/ST/SEBC). GUJCET is needed for state quota; NEET is "
                    "NOT required. Minimum age is 17 years on 31st December of the "
                    "admission year. Diploma in Pharmacy holders can join the "
                    "2nd year (Semester 3).")
        elif has(text, "m pharm", "mpharm"):
            return ("M.Pharm eligibility: B.Pharm from a PCI approved "
                    "college/university with about 50-55% (General) or 40-45% "
                    "(SC/ST/SEBC). GPAT is needed for the ACPC process but not "
                    "for the management quota.")
        else:
            return ("Eligibility depends on the course:\n"
                    "• B.E./B.Tech: 12th Science (PCMB)\n"
                    "• BCA: 12th any stream with English, 45% marks\n"
                    "• B.Pharm: 12th with PCB/PCM, 45% (General)\n"
                    "• M.Pharm: B.Pharm degree\n"
                    "Type e.g. 'BCA eligibility' for details, or call "
                    f"{ADMISSION_PHONE} for Diploma and other courses.")

    elif has(text, "admission", "admissions", "apply", "enroll", "enrol",
             "registration", "register", "join", "acpc", "seat", "seats",
             "last date", "how to apply"):
        return ("Admission 2026-27 is OPEN at GMIU.\n"
                "• Apply online: https://erp.gmiu.edu.in/admission/student-registration\n"
                "• Or visit the Admission Cell in person (10:00 AM to 06:00 PM)\n"
                "• Diploma Engineering: 50% seats through ACPC and 50% through "
                "the college Management Quota\n"
                "• ACPC-allotted students must report at the institute or call "
                "+91 90999 51160 / +91 75749 49494\n"
                "• Career expert for guidance: Prof. Mrugesh Makwana "
                "(+91 75749 49494)\n"
                "• University Transfer and Virtual Counselling are also available "
                "on the website.")

    elif has(text, "placement", "placements", "job", "jobs", "recruit",
             "recruiter", "package", "campus placement", "career"):
        return ("GMIU has a dedicated Training & Placement Cell with a "
                "Departmental Placement Officer for every branch. It organises "
                "industry visits, case studies, debate training and interview "
                "preparation, followed by placement drives.\n"
                "Placement statistics (2023 / 2024 / 2025 / 2026):\n"
                "• Computer Engineering: 98% / 87% / 98% / 98%\n"
                "• Information Technology: 94% / 94% / 93% / 94%\n"
                "• Mechanical Engineering: 100% / 100% / 100% / 100%\n"
                "• Civil Engineering: - / 83% / 76% / 70%\n"
                "Details: https://admission.gmiu.edu.in/placement")

    elif has(text, "library", "books", "reading room"):
        return ("GMIU has a well-equipped central library with recent books on "
                "every subject. Library timings are not published online, so "
                f"please call {PHONE} to confirm.\n"
                "More info: https://gmiu.edu.in/campus/library.php")

    elif has(text, "exam", "exams", "examination", "exam date", "exam dates",
             "result", "results", "time table", "timetable", "evaluation"):
        return ("Exam dates are announced through official circulars, so they are "
                "not fixed in this bot. Check: https://gmiu.edu.in/home/circular.php\n"
                "Exam pattern (Pharmacy, as per FAQ): End Semester 80 marks + "
                "Mid Semester 20 marks, plus continuous evaluation by assignments, "
                "quizzes and projects.\n"
                "GMIU follows the Proficient Learning Method (PLM) - concept-based, "
                "case-study based, module-wise exams instead of rote learning.")

    elif has(text, "attendance"):
        return ("75% attendance in BOTH theory and practical is mandatory to "
                "appear in the final university examinations of GMIU.")

    elif has(text, "timing", "timings", "time", "hours", "open", "schedule",
             "lecture time", "college time"):
        return ("The Admission Cell is open from 10:00 AM to 06:00 PM. Exact "
                "class timings differ by institute and semester and are not "
                f"published online - please call {PHONE} for your course timing.")

    elif has(text, "uniform", "dress code"):
        return ("Engineering students must wear the college uniform six days a "
                "week, and shoes are mandatory in laboratory sessions.")

    elif has(text, "safety", "security", "cctv", "ragging", "anti ragging",
             "women cell", "gender", "harassment"):
        return ("Safety at GMIU: entry only with I-Card through a single gate, "
                "CCTV surveillance across the campus, an Anti-Ragging Committee, "
                "and a Women Cell / Gender Sensitization Committee for girl "
                "students. Anti-ragging info: https://gmiu.edu.in/campus/anti-ragging.php")

    elif has(text, "facility", "facilities", "wifi", "wi fi", "cafeteria",
             "canteen", "lab", "labs", "laboratory", "laboratories",
             "classroom", "infrastructure", "campus", "sports", "cricket",
             "first aid"):
        return ("Campus facilities at GMIU:\n"
                "• 65+ laboratories and AC classrooms with LCD projectors\n"
                "• Wi-Fi campus, central library\n"
                "• Cafeteria and First Aid room\n"
                "• Box cricket and sports activities\n"
                "• Own bus fleet and boys/girls hostels\n"
                "• Continuous CCTV monitoring\n"
                "Take a 360 virtual tour: https://gmiu.edu.in/campus/360_virtual_tour.php")

    elif has(text, "event", "events", "cultural", "kalamanjari", "khelmanjari",
             "rasmanjari", "techmanjari", "activities", "nss", "club"):
        return ("GMIU organises Tech-Manjari, Kala-Manjari, Khel-Manjari and "
                "Ras-Manjari every academic year for technical, art, sports and "
                "cultural talent. There are also NSS, expert talks, industry "
                "visits, project exhibitions and the Mastermind programme.")

    elif has(text, "startup", "start up", "entrepreneur", "incubation", "gmsec"):
        return ("GMIU supports startups through the GM Startup & Entrepreneurship "
                "Cell (GMSEC), SSIP & IPR support and an annual startup pitch "
                "event with industry entrepreneurs. Students have started 7 "
                "startups so far. See: https://gmiu.edu.in/startup/about_startup.php")

    elif has(text, "research", "phd", "ph d", "doctoral", "gmrdc"):
        return ("GMIU offers Ph.D. programs (3 programs available) and has the GM "
                "Research & Development Cell (GMRDC) for research and innovation. "
                "More: https://gmiu.edu.in/research/phd_program.php")

    elif has(text, "international", "abroad", "foreign", "global"):
        return ("The GMIU International Relations Cell coordinates collaborations "
                "with foreign universities and global partners, giving students "
                "international exposure. See: "
                "https://gmiu.edu.in/international_cell/about_irc.php")

    elif has(text, "plm", "proficient learning", "learning method"):
        return ("PLM (Proficient Learning Method) is GMIU's skill-focused teaching "
                "method. Rote learning is replaced by case studies, practicals "
                "inside the classroom and module-wise concept-based exams, so "
                "students become industry-ready. "
                "Know more: https://admission.gmiu.edu.in/key-features-of-plm")

    elif has(text, "girls college", "ggc", "girls"):
        return ("GMIU has a dedicated Girls' College (GGC): https://ggc.gmiu.edu.in/\n"
                "Girl students also have a Women Cell and a girls' hostel.")

    # ---------------- 3. Courses (specific first, general last) ----------
    elif has(text, "diploma"):
        return ("Diploma Engineering at GMIU (26 diploma programs in total). "
                "Branches include:\n"
                "• Electrical, Mechanical, Civil Engineering\n"
                "• Information Technology (IT) and Computer Engineering\n"
                "• Chemical Engineering\n"
                "• Electronics & Communication Engineering\n"
                "• Computer Aided Costume Design & Dress Making\n"
                "• Interior Design\n"
                "50% seats are filled via ACPC and 50% by Management Quota. "
                "See: https://gmiu.edu.in/faculty/diploma/")

    elif has(text, "bca", "mca", "computer application"):
        if has(text, "mca"):
            return ("MCA (Master of Computer Applications) is a 2-year "
                    "post-graduate program in the Institute of Computer "
                    "Application, blending theory with practical application "
                    "development. See: https://gmiu.edu.in/bca-mca/")
        return ("BCA at GMIU is a 4-year program. Honors options: Cyber "
                "Security, Mobile Applications, Cloud Technology, Data Science "
                "and Web Technology. An Integrated BCA+MCA in 5 years is also "
                "available. Eligibility: 10+2 any stream with English, 45%.")

    elif has(text, "pharmacy", "pharm", "b pharm", "bpharm", "m pharm", "mpharm"):
        return ("Institute of Pharmacy (PCI approved):\n"
                "• B.Pharm - 4 years, 100 seats\n"
                "• M.Pharm - 2 years, 30 seats (Pharmaceutics, Pharmaceutical "
                "Quality Assurance)\n"
                "NEET is not required for B.Pharm admission. GPAT-qualified "
                "students may get the PCI scholarship of Rs. 12,400 per month.")

    elif has(text, "commerce", "bcom", "b com", "mcom", "m com"):
        return ("Institute of Commerce:\n"
                "• B.Com Honors - 3 years (Accounting & Finance, Banking & "
                "Insurance, Marketing Management, Innovation & Entrepreneurship)\n"
                "• International/Research B.Com - 4 years\n"
                "• M.Com - 2 years (Finance & Accounting, Banking & Insurance, "
                "Marketing & Management, Innovation & Business)\n"
                "A 'Genius Batch' with extra skills like Tally is also offered.")

    elif has(text, "btech", "b tech", "engineering", "cse", "ai ml",
             "computer engineering", "mechanical", "civil", "electrical"):
        return ("Institute of Engineering & Technology offers Diploma and Degree "
                "(B.E./B.Tech) programs, e.g. Computer Science with AI & ML "
                "Honors, IT, Mechanical, Civil, Electrical and Chemical. "
                "Eligibility for B.Tech is 12th Science (PCMB). "
                "See: https://gmiu.edu.in/engineering/")

    elif has(text, "institute", "institutes", "faculty", "faculties",
             "department", "departments", "school", "schools"):
        return ("GMIU has 10 institutes:\n"
                "• Engineering & Technology (Diploma)\n"
                "• Engineering & Technology (Degree)\n"
                "• Pharmacy  • Science  • Commerce  • Management\n"
                "• Arts  • Computer Application (BCA/MCA)\n"
                "• Design  • Law (LL.B.)")

    elif has(text, "course", "courses", "program", "programs", "programme",
             "branch", "branches", "degree", "ug", "pg", "undergraduate",
             "postgraduate", "stream", "streams"):
        return ("GMIU offers:\n"
                "• Diploma - 26 programs\n"
                "• Undergraduate (UG) - 133 programs\n"
                "• Postgraduate (PG) - 90 programs\n"
                "• Ph.D. - 3 programs\n"
                "Across Engineering, Pharmacy, Science, Commerce, Management, "
                "Arts, BCA/MCA, Design and Law.\n"
                "Ask about a specific one, e.g. 'diploma courses', 'BCA', "
                "'B.Pharm'. Full list: https://gmiu.edu.in/faculty/all_programs.php")

    # ---------------- 4. Contact & about ----------------
    elif has(text, "contact", "phone", "call", "mobile", "number", "email",
             "mail", "address", "location", "where", "reach", "map",
             "whatsapp", "website"):
        return (f"GMIU contact details:\n"
                f"• Phone: {PHONE}\n"
                f"• Admission / WhatsApp: {ADMISSION_PHONE}\n"
                f"• Email: {EMAIL}\n"
                f"• Address: {ADDRESS}\n"
                f"• Website: {WEBSITE}")

    elif has(text, "about", "gmiu", "gyanmanjari", "university", "college",
             "tell me", "established", "founded", "history", "overview"):
        return ("Gyanmanjari Innovative University (GMIU) is a private "
                "university in Bhavnagar, Gujarat, established in 2015. It "
                "offers industry-aligned programs in Engineering, Pharmacy, "
                "Science, Commerce, Management, Arts, BCA/MCA, Design and Law "
                "through the Proficient Learning Method (PLM).\n"
                "GMIU at a glance: 208+ subjects, 3000+ students, 65+ "
                "laboratories and 300+ faculty members.\n"
                f"Address: {ADDRESS}")

    # ---------------- 5. Nothing matched ----------------
    else:
        return FALLBACK


def main():
    """Terminal version of the chatbot (uses input(), print() and a loop)."""
    print("=" * 60)
    print(f"  {BOT_NAME} - GMIU College Help Chatbot")
    print("  Type 'bye' or 'exit' to quit.")
    print("=" * 60)
    print(f"{BOT_NAME}: {WELCOME}\n")

    while True:
        user_input = input("You: ")
        reply = get_response(user_input)
        print(f"\n{BOT_NAME}: {reply}\n")

        if has(user_input.lower(), "bye", "goodbye", "exit", "quit"):
            break


if __name__ == "__main__":
    main()
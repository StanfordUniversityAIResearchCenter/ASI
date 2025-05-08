"""
محاكاة مبسطة للذكاء الاصطناعي الخارق (ASI)

النموذج يضم:
- قاعدة معرفة لتعلم الحقائق.
- آليات استدلال متعددة (الاستنتاج، الحث، الاستنباط).
- تحسين ذاتي لضبط آليات الاستدلال.
- اتخاذ قرارات مبنية على آليات التفكير.

ملاحظة: هذا نموذج تعليمي رمزي وليس ذكاءً اصطناعيًا حقيقيًا خارقًا.
"""

import random

class ASI:
    def __init__(self):
        # قاعدة المعرفة كـمجموعة من الحقائق النصية
        self.knowledge = set()
        # أوزان آليات الاستدلال
        self.heuristics = {
            'deduction': 1.0,  # الاستنتاج
            'induction': 1.0,  # الحث
            'abduction': 1.0,  # الاستنباط
        }
        self.reasoning_trace = []

    def learn(self, new_facts):
        """اضافة حقائق جديدة الى قاعدة المعرفة"""
        before = len(self.knowledge)
        for fact in new_facts:
            self.knowledge.add(fact.lower())
        after = len(self.knowledge)
        print(f"تم تعلم {after - before} حقيقة جديدة.")

    def reason(self, query):
        """
        محاولة الاجابة على سؤال بناءً على قاعدة المعرفة وطرق الاستدلال.
        تعيد: (هل تم إيجاد جواب, درجة الثقة)
        """
        self.reasoning_trace.clear()
        query = query.lower()

        # الاستنتاج: تحقق مباشر من وجود حقيقة مطابقة
        if query in self.knowledge:
            self.reasoning_trace.append("استنتاج: وجد تطابق مباشر في قاعدة المعرفة.")
            confidence = 0.9 * self.heuristics['deduction']
            return True, confidence

        # الحث: تحقق من وجود كلمات مشابهة في الحقائق
        related = [fact for fact in self.knowledge if query in fact]
        if related:
            self.reasoning_trace.append("حث: وجدت حقائق ذات علاقة تحتوي على كلمة البحث.")
            confidence = min(0.5 + 0.1 * len(related), 0.85) * self.heuristics['induction']
            return True, confidence

        # الاستنباط: تخمين بأقل ثقة
        self.reasoning_trace.append("استنباط: لا توجد معرفة مباشرة أو ذات علاقة، تم التخمين بأفضل شكل.")
        confidence = 0.3 * self.heuristics['abduction']
        return False, confidence

    def self_improve(self):
        """تحسين ذاتي عبر زيادة وزن إحدى آليات الاستدلال بشكل عشوائي"""
        heuristic_to_improve = random.choice(list(self.heuristics.keys()))
        change = random.uniform(0.01, 0.05)
        old_value = self.heuristics[heuristic_to_improve]
        new_value = min(old_value + change, 2.0)  # الحد الأعلى
        self.heuristics[heuristic_to_improve] = new_value
        improvement_msg = f"تحسين ذاتي: زيادة وزن '{heuristic_to_improve}' من {old_value:.3f} إلى {new_value:.3f}."
        self.reasoning_trace.append(improvement_msg)
        print(improvement_msg)

    def decision(self, problem):
        """اتخاذ قرار مبسط مع شرح خطوات التفكير"""
        print(f"معالجة المشكلة: \"{problem}\"")
        keywords = problem.lower().split()
        confidence_scores = []
        knowledge_hits = 0

        for kw in keywords:
            found, confidence = self.reason(kw)
            confidence_scores.append(confidence)
            if found:
                knowledge_hits += 1
            print(f"الكلمة المفتاحية '{kw}': تم العثور={found}, درجة الثقة={confidence:.2f}")
            for step in self.reasoning_trace:
                print(" - " + step)
            self.reasoning_trace.clear()

        avg_conf = sum(confidence_scores) / len(confidence_scores) if confidence_scores else 0
        print(f"متوسط درجة الثقة: {avg_conf:.2f}")

        if avg_conf > 0.7:
            decision = "نعم"
            reason = "ثقة عالية بناءً على معرفة واسعة."
        elif avg_conf > 0.4:
            decision = "ربما"
            reason = "ثقة متوسطة، بعض الفجوات المعرفية."
        else:
            decision = "لا"
            reason = "ثقة منخفضة، المعرفة غير كافية."

        final_decision = f"القرار: {decision} - {reason}"
        print(final_decision)
        return final_decision


if __name__ == "__main__":
    asi = ASI()
    asi.learn([
        "الماء يتجمد عند درجة صفر مئوية.",
        "الأرض تدور حول الشمس.",
        "البشر يحتاجون إلى الأكسجين للبقاء على قيد الحياة.",
        "النار ساخنة وتسبب حروقاً.",
        "النباتات تستخدم التمثيل الضوئي لإنتاج الغذاء."
    ])

    problems = [
        "هل يمكن تجميد الماء؟",
        "هل الأرض مسطحة؟",
        "هل يستطيع الإنسان التنفس تحت الماء دون معدات؟",
        "هل النار باردة؟",
        "هل تنتج النباتات الأكسجين؟"
    ]

    for problem in problems:
        asi.decision(problem)
        print()

    for i in range(3):
        print(f"\nدورة تحسين ذاتي رقم {i+1}")
        asi.self_improve()

</content>
</create_file>

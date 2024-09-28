class Character:
    def __init__(self, name, hp, ap, dp, sp, mp, image_path, job_class):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.ap = ap
        self.dp = dp
        self.sp = sp
        self.mp = mp
        self.image_path = image_path
        self.job_class = job_class
        self.defend_turns = 0

    def attack(self, target):
        damage = self.ap - target.dp
        if damage > 0:
            target.take_damage(damage)

    def defend(self):
        self.dp *= 1.5
        self.defend_turns = 1
        if self.dp>=10:
            self.dp=10
            

    def heal(self):
        if self.mp >= 20:
            healed_amount = int(self.max_hp * 0.2)  # Restores 20% of maximum HP
            self.hp = min(self.hp + healed_amount, self.max_hp)
            self.mp -= 20

    def take_damage(self, damage):
        if self.defend_turns > 0:
            damage = max(damage - self.dp, 0)
            self.defend_turns = 0
        self.hp = max(0, self.hp - damage)
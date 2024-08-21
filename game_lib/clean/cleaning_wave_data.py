from dataclasses import dataclass, field

from ..res_base import BaseRes


@dataclass
class CleaningWaveData(BaseRes):
    remainTime: int = field(default=30)
    nextWave: int = field(default=1)
    normalEnemyCount: int = field(default=4)
    rareEnemyCount: int = field(default=0)
    getTotalEnemyDown: int = field(default=0)
    specialAttackAdditionValue: int = field(default=3)
    specialAttackMaxValue: int = field(default=100)
    specialAttackBonusRate: int = field(default=100)
    normalEnemyApRecoveryValue: int = field(default=1)
    rareEnemyApRecoveryValue: int = field(default=1)
    normalEnemyExpValue: int = field(default=0)
    rareEnemyExpValue: int = field(default=0)
    enemyExpBonusRate: int = field(default=200)

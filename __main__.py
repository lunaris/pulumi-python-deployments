import pulumi
import pulumi_random

r = pulumi_random.RandomString("r", length=10)

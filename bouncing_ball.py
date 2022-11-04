from ursina import *
import random

app = Ursina()

side = 3.0
thickness = 0.2
s2 = 2 * side - thickness
s3 = 2 * side + thickness

wallRight = Entity(model="cube", position=Vec3(side, 0, 0), scale=Vec3(thickness, s2, s3), color=color.red)
wallLeft = Entity(model="cube", position=Vec3(-side, 0, 0), scale=Vec3(thickness, s2, s3), color=color.red)
wallBottom = Entity(model="cube", position=Vec3(0, -side, 0), scale=Vec3(s3, thickness, s3), color=color.blue)
wallTop = Entity(model="cube", position=Vec3(0, side, 0), scale=Vec3(s3, thickness, s3), color=color.blue)
wallBack = Entity(model="cube", position=Vec3(0, 0, side), scale=Vec3(s2, s2, thickness), color=color.gray)

ball = Entity(model="sphere", color=color.green, scale=Vec3(0.4, 0.4, 0.4), collider="sphere")
ball.velocity = Vec3(-5, -2, 7)

size = side - thickness * 0.5 - ball.scale.x

applesList = [Entity(model="sphere",
                 color=color.orange,
                 position=Vec3(random.uniform(-size, size), random.uniform(-size, size), random.uniform(-size, size)),
                 scale=Vec3(0.3, 0.3, 0.3),
                 collider="sphere") for _ in range(10)]


def update():
    ball.position += ball.velocity * time.dt

    if ball.x < -size or ball.x > size:
        ball.velocity.x *= -1

    if ball.y < -size or ball.y > size:
        ball.velocity.y *= -1

    if ball.z < -size or ball.z > size:
        ball.velocity.z *= -1

    for apple in applesList[:]:
        if ball.intersects(apple).hit:
            ball.scale *= 1.1
            destroy(apple)
            applesList.remove(apple)


app.run()

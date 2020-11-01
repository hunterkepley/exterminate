import pygame
import game_handler
import sprayer

def update_game(g, dt):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            g.running = False
        if event.type == pygame.MOUSEBUTTONUP:
            if g.placing:
                if g.placer.object == 0:
                    if g.store.money >= g.store.prices['sprayer']:
                        game_handler.sprayer.Sprayer.spawn_sprayer(g, g.placer.position)
                        g.store.money -= g.store.prices['sprayer']
                elif g.placer.object == 1:
                    if g.store.money >= g.store.prices['stickypad']:
                        game_handler.sticky_pad.StickyPad.spawn_sticky_pad(g, g.placer.position)
                        g.store.money -= g.store.prices['stickypad']
        if event.type == pygame.KEYDOWN:
            object_images = {
                0: './Assets/object_sprayer.png',
                1: './Assets/object_gluepad.png'
            }
            if event.key == pygame.K_LEFT and g.placer.object > 0:
                g.placer.object -= 1
            elif event.key == pygame.K_RIGHT and g.placer.object < len(g.placer.objects)-1:
                g.placer.object += 1
            g.object_image = pygame.image.load(object_images[g.placer.object])
    
    if g.placing:
        g.placer.update(g, dt)

    game_handler.bug.Bug.update_bugs(g, dt)

    game_handler.sprayer.Sprayer.update_sprayers(g, dt)

    game_handler.sticky_pad.StickyPad.update_sticky_pads(g, dt)

    game_handler.bug.Bug.bug_spawn_handler(g)

    # FPS Printing
    #print(g.clock.get_fps())
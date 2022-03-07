from math import floor
import random
import pygame
from champ import *

class PokeLol:

    global color_0, color_1, color_2, color_3, color_4, white, black, user, guest

    color_0 = (38, 70, 83)
    color_1 = (42, 157, 143)
    color_2 = (233, 196, 106)
    color_3 = (244, 162, 97)
    color_4 = (231, 111, 81)
    white = (255, 255, 255)
    black = (0, 0, 0)
    user = Lux()
    guest = Vi()

    def __init__(self, x=640, y=480):
        self.x = x
        self.y = y

        self.display = pygame.display.set_mode((self.x, self.y))
        self.clock = pygame.time.Clock()
        img = pygame.image.load("assets/images/favicon.png").convert_alpha()
        pygame.display.set_icon(img)
        pygame.display.set_caption("League of Pokemon")

    def homepage(self):
        img = pygame.image.load("assets/images/homepage.jpeg")
        img = pygame.transform.scale(img, (self.x, self.y))
        img_rect = img.get_rect(center=((self.x / 2), (self.y / 2)))

        title = pygame.font.Font("assets/fonts/SCRUBLAND.ttf", 50)
        title = title.render("LEAGUE OF POKEMON", True, color_0)
        title_rect = title.get_rect(midtop=((self.x / 2), 50))

        play_btn = pygame.Rect((self.x / 2) - (150 / 2), (self.y / 1.5) - (50 / 2), 150, 50)
        leave_btn = pygame.Rect((self.x / 2) - (150 / 2), (self.y / 1.25) - (50 / 2), 150, 50)
        play_text, play_rect = self.write_title("PLAY", 2, 1.5, white)
        leave, leave_rect = self.write_title("QUIT", 2, 1.25, white)

        self.display.blit(img, img_rect)
        self.display.blit(title, title_rect)

        if play_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, color_1, play_btn, border_radius = 2)
            if pygame.mouse.get_pressed() == (True, False, False):
                return True
        else:
            pygame.draw.rect(self.display, color_0, play_btn, border_radius = 2)

        if leave_btn.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(self.display, color_3, leave_btn, border_radius = 2)
            if pygame.mouse.get_pressed() == (True, False, False):
                pygame.quit()
        else:
            pygame.draw.rect(self.display, color_4, leave_btn, border_radius = 2)
        
        self.display.blit(play_text, play_rect)
        self.display.blit(leave, leave_rect)

        return False

    def write_title(self, text, x, y, color, size=20):
        self.font = pygame.font.Font("assets/fonts/SCRUBLAND.ttf", size)
        text = self.font.render(text, True, color)
        text_rect = text.get_rect(center=(self.x / x, (self.y / y)))
        return text, text_rect

    def write(self, text, x, y, color, size=10):
        self.font = pygame.font.Font("assets/fonts/PublicPixel.ttf", size)
        text = self.font.render(text, True, color)
        text_rect = text.get_rect(center=(self.x / x, (self.y / y)))
        return text, text_rect
    
    def play(self):
        user.live = 100
        guest.live = 100
        txt, txt_rect = self.write_title("FIGHT", 2, 2, white, 75)
        img = pygame.image.load("assets/images/background.jpeg")
        img = pygame.transform.scale(img, (self.x, self.y))
        img_rect = img.get_rect(center=((self.x / 2), (self.y / 2)))
        self.display.blit(img, img_rect)
        self.display.blit(txt, txt_rect)
        pygame.display.update()
        pygame.time.wait(1000)

        self.display.blit(img, img_rect)
        user_img, user_rect = self.user_champ()
        guest_img, guest_rect = self.guest_champ()
        self.display.blit(user_img, user_rect)
        self.display.blit(guest_img, guest_rect)
        pygame.display.update()

        while True:
            a = 4
            user_txt, user_txt_rect = self.write(user.init, 1.75, 1.25, black)
            guest_txt, guest_txt_rect = self.write(guest.init, 2.5, 12.5, black)
            user_bg = pygame.Rect(10, 10, (self.x - user_img.get_size()[0]), 100)
            guest_bg = pygame.Rect((236 / 2) + 10, (self.y - (236 / 2)) - 10, (self.x - guest_img.get_size()[0]), 100)
            b1 = pygame.Rect(((self.x / 2) - 50) * 0.25, (self.y / 2) - 50, 100, 100)
            b2 = pygame.Rect(((self.x / 2) - 50) * 1, (self.y / 2) - 50, 100, 100)
            b3 = pygame.Rect(((self.x / 2) - 50) * 1.75, (self.y / 2) - 50, 100, 100)

            if (user.live == 0) or (guest.live == 0):
                break

            if b1.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.display, color_1, b1, border_radius = 100)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    while ((a > 3) or (a == 0)):
                        a = floor(random.random()*10)
                    self.verification(1, a)
            else:
                pygame.draw.rect(self.display, color_0, b1, border_radius = 100)
            
            if b2.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.display, color_1, b2, border_radius = 100)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    while ((a > 3) or (a == 0)):
                        a = floor(random.random()*10)
                    self.verification(2, a)
            else:
                pygame.draw.rect(self.display, color_0, b2, border_radius = 100)
            
            if b3.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.display, color_1, b3, border_radius = 100)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    while ((a > 3) or (a == 0)):
                        a = floor(random.random()*10)
                    self.verification(3, a)
            else:
                pygame.draw.rect(self.display, color_0, b3, border_radius = 100)

            force_img = pygame.image.load("assets/images/strength.png", "Force")
            force_img = pygame.transform.scale(force_img, (75, 75))
            force_rect = force_img.get_rect(midleft=(((self.x / 2) * 0.25) - 2, (self.y / 2))) #image non centré d'origine* => retrait de 2 pixel vers la gauche

            shield_img = pygame.image.load("assets/images/shield.png", "Bouclier")
            shield_img = pygame.transform.scale(shield_img, (75, 75))
            shield_rect = shield_img.get_rect(center=((self.x / 2) * 1, (self.y / 2)))

            magic_img = pygame.image.load("assets/images/magic.png", "Magie")
            magic_img = pygame.transform.scale(magic_img, (75, 75))
            magic_rect = magic_img.get_rect(midright=((self.x / 2) * 1.75, (self.y / 2)))

            user_hp_back, user_hp = self.health_bar(10 ,(self.y / 1.5) + 20, user.live)
            pygame.draw.rect(self.display, color_3, user_hp_back, border_radius=5)
            pygame.draw.rect(self.display, color_4, user_hp, border_radius=5)

            guest_hp_back, guest_hp = self.health_bar((self.x - 120), (236 / 2), guest.live)
            pygame.draw.rect(self.display, color_3, guest_hp_back, border_radius=5)
            pygame.draw.rect(self.display, color_4, guest_hp, border_radius=5)

            self.display.blit(force_img, force_rect)
            self.display.blit(magic_img, magic_rect)
            self.display.blit(shield_img, shield_rect)

            pygame.draw.rect(self.display, white, user_bg, border_radius=10)
            pygame.draw.rect(self.display, white, guest_bg, border_radius=10)
            self.display.blit(user_txt, user_txt_rect)
            self.display.blit(guest_txt, guest_txt_rect)
            
            pygame.display.update()
            self.clock.tick(60)

            if pygame.event.get(pygame.QUIT):
                return False

        if user.live == 0:
            self.game_over()
        elif guest.live == 0:
            self.win()
            
    def user_champ(self):
        img_champ = pygame.image.load("assets/images/champ/vi.png")
        img_champ = pygame.transform.scale(img_champ, ((self.x / 4), (self.y / 4)))
        img_rect = img_champ.get_rect(bottomleft=(0, self.y))
        return img_champ, img_rect

    def guest_champ(self):
        img_champ = pygame.image.load("assets/images/champ/vi.png")
        img_champ = pygame.transform.scale(img_champ, ((self.x / 4), (self.y / 4)))
        img_rect = img_champ.get_rect(topright=(self.x, 0))
        return img_champ, img_rect

    def verification(self, user_play, guest_play):
        if user_play == guest_play:
            user.get_null()
            guest.get_null()
        elif (user_play, guest_play) in ((3, 1), (2, 3), (1, 2)):
            guest.get_attack()
        else:
            user.get_attack()

    def health_bar(self, x, y, heal):
        hp_back = pygame.Rect(x, y, 100, 20)
        hp = pygame.Rect(x, y, heal, 20)
        return hp_back, hp
    
    def game_over(self):
        while True:
            img = pygame.image.load("assets/images/homepage.jpeg")
            img = pygame.transform.scale(img, (self.x, self.y))
            img_rect = img.get_rect(center=((self.x / 2), (self.y / 2)))
            txt = pygame.font.Font("assets/fonts/SCRUBLAND.ttf", 50)
            txt = txt.render("YOU LOOSE POOR NOOB !", True, color_0)
            txt_rect = txt.get_rect(midtop=((self.x / 2), 0))
            play_again, play_again_rect = self.write_title("Play again ?", 2, 2, white, 24)
            play_again_btn = pygame.Rect((self.x / 2) - (250 / 2), (self.y / 2) - (75 / 2), 250, 75)
            homepage_txt, homepage_txt_rect = self.write_title("Back to menu", 2, 1.5, white, 24)
            homepage_btn = pygame.Rect((self.x / 2) - (250 / 2), (self.y / 1.5) - (75 / 2), 250, 75)

            self.display.blit(img, img_rect)
            self.display.blit(txt, txt_rect)

            if play_again_btn.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.display, color_1, play_again_btn, border_radius=100)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    self.play()
            else:
                pygame.draw.rect(self.display, color_0, play_again_btn, border_radius=100)

            if homepage_btn.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.display, color_3, homepage_btn, border_radius=100)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    self.homepage()
            else:
                pygame.draw.rect(self.display, color_4, homepage_btn, border_radius=100)
                
            self.display.blit(play_again, play_again_rect)
            self.display.blit(homepage_txt, homepage_txt_rect)

            pygame.display.update()
            if pygame.event.get(pygame.QUIT):
                break

    def win(self):
        while True:
            img = pygame.image.load("assets/images/homepage.jpeg")
            img = pygame.transform.scale(img, (self.x, self.y))
            img_rect = img.get_rect(center=((self.x / 2), (self.y / 2)))
            txt = pygame.font.Font("assets/fonts/SCRUBLAND.ttf", 50)
            txt = txt.render("YOU DID IT, CHAMPION !", True, color_0)
            txt_rect = txt.get_rect(midtop=((self.x / 2), 0))
            play_again, play_again_rect = self.write_title("Play again ?", 2, 2, white, 24)
            play_again_btn = pygame.Rect((self.x / 2) - (250 / 2), (self.y / 2) - (75 / 2), 250, 75)
            homepage_txt, homepage_txt_rect = self.write_title("Back to menu", 2, 1.5, white, 24)
            homepage_btn = pygame.Rect((self.x / 2) - (250 / 2), (self.y / 1.5) - (75 / 2), 250, 75)

            self.display.blit(img, img_rect)
            self.display.blit(txt, txt_rect)

            if play_again_btn.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.display, color_1, play_again_btn, border_radius=100)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    self.play()
            else:
                pygame.draw.rect(self.display, color_0, play_again_btn, border_radius=100)

            if homepage_btn.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.display, color_3, homepage_btn, border_radius=100)
                if pygame.event.get(pygame.MOUSEBUTTONDOWN):
                    self.homepage()
            else:
                pygame.draw.rect(self.display, color_4, homepage_btn, border_radius=100)
                
            self.display.blit(play_again, play_again_rect)
            self.display.blit(homepage_txt, homepage_txt_rect)

            pygame.display.update()
            if pygame.event.get(pygame.QUIT):
                break
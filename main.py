import pygame, sys, random, asyncio, math
from pygame.locals import *
from resources.classes.bullet import Bullet
from resources.classes.enemies import Enemy
from resources.classes.reference_classes import Button, MultilineText
from resources.start_screen import Start_screen, Instructions_Screen, Credits_Screen
from resources.end_screen import End_screen, Completed_Screen
from resources.difficulty_screen import Difficulty_Screen
from resources.settings_screen import Settings_Screen

pygame.mixer.pre_init(44100, -16, 1, 512)

pygame.init()

#Sound Channels
spell_cast_channel = pygame.mixer.find_channel()
enemy_hit_channel = pygame.mixer.find_channel()
purple_charging_channel = pygame.mixer.find_channel()
game_sound_channel = pygame.mixer.find_channel()
coin_sound_channel = pygame.mixer.find_channel()
levelup_sound_channel = pygame.mixer.find_channel()
roundpassed_sound_channel = pygame.mixer.find_channel()
enemy_damage_channel = pygame.mixer.find_channel()\

#Sounds
coin_sound = pygame.mixer.Sound("resources/audio/coin_sound.ogg") #
bang_sound = pygame.mixer.Sound("resources/audio/bang_sound.ogg") #
kaching_sound = pygame.mixer.Sound("resources/audio/ka-ching_sound.ogg") #
error_sound = pygame.mixer.Sound("resources/audio/error_sound.ogg") #
levelup_sound = pygame.mixer.Sound("resources/audio/levelup_sound.ogg") #
roundpassed_sound = pygame.mixer.Sound("resources/audio/roundpassed_sound.ogg") #
fail_sound = pygame.mixer.Sound("resources/audio/fail_sound.ogg") #
black_sound = pygame.mixer.Sound("resources/audio/black_sound.ogg") #
green_sound = pygame.mixer.Sound("resources/audio/green_sound.ogg") #
red_sound = pygame.mixer.Sound("resources/audio/red_sound.ogg") #
blue_sound = pygame.mixer.Sound("resources/audio/blue_sound.ogg") #
yellow_sound = pygame.mixer.Sound("resources/audio/yellow_sound.ogg") #
rainbow_sound = pygame.mixer.Sound("resources/audio/rainbow_sound.ogg") #
page_flip = pygame.mixer.Sound("resources/audio/page_flip.ogg") #
damage_sound = pygame.mixer.Sound("resources/audio/damage_sound.ogg") #
purple_charging = pygame.mixer.Sound("resources/audio/purple_charging.ogg") #
door_open = pygame.mixer.Sound("resources/audio/door_open_sound.ogg") #
door_close = pygame.mixer.Sound("resources/audio/door_close_sound.ogg") #
info_open_sound = pygame.mixer.Sound("resources/audio/info_open_sound.ogg") #
info_close_sound = pygame.mixer.Sound("resources/audio/info_close_sound.ogg") #

sfx = [coin_sound, bang_sound, kaching_sound, levelup_sound, roundpassed_sound, fail_sound, black_sound, green_sound, red_sound, blue_sound, yellow_sound, rainbow_sound, page_flip, damage_sound, purple_charging, door_close, door_open, info_close_sound, info_open_sound]

#Music
game_music = "resources/audio/game_music.ogg"
menu_music = "resources/audio/menu_music.ogg"

#Settings
settings = {"volume":75, 
            "music": 1,
            "sfx": 1,
            "camera_shake":1,
            "hitboxes":0, 
            "ne":1}
settings_previous_screen = "ss"




# Colours
COLOR_BACKGROUND = (0, 0, 0)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()

#Game Dimensions
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 800

MIDDLE_X = WINDOW_WIDTH//2
MIDDLE_Y = WINDOW_HEIGHT//2

BACKGROUND_WIDTH = 2000
BACKGROUND_HEIGHT = 2000

PLAYER_WIDTH = 64
PLAYER_HEIGHT = 128
PLAYER_FRAME_DELAY = 5

HITBOX_WIDTH = 2

CURSOR_WIDTH = 16
CURSOR_HEIGHT = 16
CURSOR_X_OFFSET = -8
CURSOR_Y_OFFSET = -8

#General Settings
BULLET_SPEED = 20

SPAWN_RADIUS = 100

ROUNDS_TEXT_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 32)
ROUND_TEXT_COORDS = (MIDDLE_X, 50)

CAMERA_MOVEMENT_VALUE = 0.05


#Coordinates
COORD_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 32)
COORD_COLOR = (125, 125, 125)
X_COORD_TEXT_X, X_COORD_TEXT_Y = 25, 50
Y_COORD_TEXT_X, Y_COORD_TEXT_Y = 25, 100

#Money
MONEY_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 32)
MONEY_TEXT_COLOR = (0, 255, 0)
MONEY_TEXT_OFFSET = 25

#MANA BAR
MANA_BAR_COORDS = (200, 640)
MANA_BAR_DIMENSIONS = (800, 15)
MANA_BAR_COLOR = (100, 100, 255)
MANA_BAR_BACK_COLOR = (0, 0, 150)

#Shop Button
SHOP_BUTTON_X = 25
SHOP_BUTTON_Y = 300
SHOP_BUTTON_WIDTH = 150
SHOP_BUTTON_HEIGHT = 75
SHOP_BUTTON_COLOR = (66, 161, 245)
SHOP_BUTTON_HOVER_COLOR = (140, 201, 255)
SHOP_BUTTON_CLICK_COLOR = (0, 92, 173)
SHOP_BUTTON_BORDER_WIDTH = 5
SHOP_BUTTON_BORDER_COLOR = (0, 0, 0)
SHOP_BUTTON_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 32)
SHOP_BUTTON_TEXT_COLOR = (0, 0, 0)
SHOP_BUTTON_TEXT_YOFFSET = 5

#Info Button
INFO_BUTTON_COORDS = (25, 385)
INFO_BUTTON_DIMENSIONS = (100, 50)
INFO_BUTTON_COLOR = (150, 0, 150)
INFO_BUTTON_HOVER_COLOR = (170, 0, 170)
INFO_BUTTON_CLICK_COLOR = (100, 0, 100)
INFO_BUTTON_BORDER_WIDTH = 5
INFO_BUTTON_BORDER_COLOR = (0, 0, 0)
INFO_BUTTON_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 10)
INFO_BUTTON_TEXT_COLOR = (0, 0, 0)
INFO_BUTTON_TEXT_YOFFSET = 3


#Info Screen
INFO_BG_RECT_ALPHA = 200
INFO_BG_OFFSET = 125
INFO_BG_COLOR = (255, 255, 255)

INFO_CLOSE_BUTTON_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 25)
INFO_CLOSE_BUTTON_DIMENSIONS = (50, 75)
INFO_CLOSE_BUTTON_POSITION = (950, 175)

INFO_PICTURE_COORDS = (200, 200)
INFO_PICTURE_DIMENSIONS = (400, 400)

INFO_TITLE_COORDS = (775, 225)
INFO_TITLE_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 32)

INFO_DBUTTON_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 25)
INFO_DBUTTON_COLOR = (255, 219, 171)
INFO_DBUTTON_HOVER_COLOR = (255, 255, 220)
INFO_DBUTTON_PRESSED_COLOR = (220, 200, 150)
INFO_DBUTTON_TEXT_COLOR = (0, 0, 0)

INFO_LEFT_BUTTON_COORDS = (200, 350)
INFO_LEFT_BUTTON_DIMENSIONS = (50, 100)

INFO_RIGHT_BUTTON_COORDS = (950, 350)
INFO_RIGHT_BUTTON_DIMENSIONS = (50, 100)

INFO_TEXT_ENTRY_DIMENSIONS = (310, 300)
INFO_TEXT_ENTRY_COORDS = (620, 250)




#Healthbar
HEALTHBAR_WIDTH = 800
HEALTHBAR_HEIGHT = 50
HEALTHBAR_X = 200
HEALTHBAR_Y = 650
HEALTHBAR_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 25)

#Cooldown Rect
COOLDOWN_RECT_DIMENSIONS = (35, 5)
COOLDOWN_RECT_YOFFSET = 5
COOLDOWN_RECT_BACK_COLOR = (200, 200, 200)
COOLDOWN_RECT_FRONT_COLOR = (100, 100, 100)

#Shop Screen
SHOP_BG_RECT_ALPHA = 200

SHOP_BG_OFFSET = 125
SHOP_BG_COLOR = (255, 255, 255)

SHOP_CLOSE_BUTTON_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 25)
SHOP_CLOSE_BUTTON_DIMENSIONS = (100, 60)
SHOP_CLOSE_BUTTON_POSITION = (925, 200)

SHOP_ITEM_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 20)
SHOP_SUB_FONT = pygame.font.Font('resources/fonts/fff-forward.regular.ttf', 15)

#Shop Buttons
SHOP_DAMAGE_BTN_COLOR = (255, 255, 255)
SHOP_DAMAGE_BTN_DIMENSIONS = (100, 100)
SHOP_DAMAGE_BTN_POSITION = (175, 250)
SHOP_DAMAGE_BTN_TITLE = SHOP_ITEM_FONT.render("Damage", True, (0, 0, 0))
shop_damage_btn_title_rect = SHOP_DAMAGE_BTN_TITLE.get_rect()
shop_damage_btn_title_rect.center = (SHOP_DAMAGE_BTN_POSITION[0]+SHOP_DAMAGE_BTN_DIMENSIONS[0]//2, SHOP_DAMAGE_BTN_POSITION[1]-25)

SHOP_MONEY_BTN_COLOR = (255, 255, 255)
SHOP_MONEY_BTN_DIMENSIONS = (100, 100)
SHOP_MONEY_BTN_POSITION = (175, 500)
SHOP_MONEY_BTN_TITLE = SHOP_ITEM_FONT.render("$ Mult.", True, (0, 0, 0))
shop_money_btn_title_rect = SHOP_MONEY_BTN_TITLE.get_rect()
shop_money_btn_title_rect.center = (SHOP_MONEY_BTN_POSITION[0]+SHOP_MONEY_BTN_DIMENSIONS[0]//2, SHOP_MONEY_BTN_POSITION[1]-25)

SHOP_GRN_BTN_COLOR = (0, 128, 82)
SHOP_GRN_BTN_DIMENSIONS = (100, 100)
SHOP_GRN_BTN_POSITION = (325, 250)
SHOP_GRN_BTN_TITLE = SHOP_ITEM_FONT.render("Health", True, (0, 0, 0))
shop_grn_btn_title_rect = SHOP_GRN_BTN_TITLE.get_rect()
shop_grn_btn_title_rect.center = (SHOP_GRN_BTN_POSITION[0]+SHOP_GRN_BTN_DIMENSIONS[0]//2, SHOP_GRN_BTN_POSITION[1]-25)

SHOP_DASH_BTN_COLOR = (0, 128, 82)
SHOP_DASH_BTN_DIMENSIONS = (100, 100)
SHOP_DASH_BTN_POSITION = (325, 500)
SHOP_DASH_BTN_TITLE = SHOP_ITEM_FONT.render("Dash", True, (0, 0, 0))
shop_dash_btn_title_rect = SHOP_DASH_BTN_TITLE.get_rect()
shop_dash_btn_title_rect.center = (SHOP_DASH_BTN_POSITION[0]+SHOP_DASH_BTN_DIMENSIONS[0]//2, SHOP_DASH_BTN_POSITION[1]-25)

SHOP_ATKSPD_BTN_COLOR = (194, 0, 0)
SHOP_ATKSPD_BTN_DIMENSIONS = (100, 100)
SHOP_ATKSPD_BTN_POSITION = (475, 250)
SHOP_ATKSPD_BTN_TITLE = SHOP_ITEM_FONT.render("Atk Spd", True, (0, 0, 0))
shop_atkspd_btn_title_rect = SHOP_ATKSPD_BTN_TITLE.get_rect()
shop_atkspd_btn_title_rect.center = (SHOP_ATKSPD_BTN_POSITION[0]+SHOP_ATKSPD_BTN_DIMENSIONS[0]//2, SHOP_ATKSPD_BTN_POSITION[1]-25)

SHOP_MANA_BTN_COLOR = (194, 0, 0)
SHOP_MANA_BTN_DIMENSIONS = (100, 100)
SHOP_MANA_BTN_POSITION = (475, 500)
SHOP_MANA_BTN_TITLE = SHOP_ITEM_FONT.render("Mana", True, (0, 0, 0))
shop_mana_btn_title_rect = SHOP_MANA_BTN_TITLE.get_rect()
shop_mana_btn_title_rect.center = (SHOP_MANA_BTN_POSITION[0]+SHOP_MANA_BTN_DIMENSIONS[0]//2, SHOP_MANA_BTN_POSITION[1]-25)

SHOP_SPD_BTN_COLOR = (0, 91, 207)
SHOP_SPD_BTN_DIMENSIONS = (100, 100)
SHOP_SPD_BTN_POSITION = (625, 250)
SHOP_SPD_BTN_TITLE = SHOP_ITEM_FONT.render("Speed", True, (0, 0, 0))
shop_spd_btn_title_rect = SHOP_SPD_BTN_TITLE.get_rect()
shop_spd_btn_title_rect.center = (SHOP_SPD_BTN_POSITION[0]+SHOP_SPD_BTN_DIMENSIONS[0]//2, SHOP_SPD_BTN_POSITION[1]-25)

SHOP_PIERCE_BTN_COLOR = (244, 196, 0)
SHOP_PIERCE_BTN_DIMENSIONS = (100, 100)
SHOP_PIERCE_BTN_POSITION = (775, 250)
SHOP_PIERCE_BTN_TITLE = SHOP_ITEM_FONT.render("PIERCE", True, (0, 0, 0))
shop_pierce_btn_title_rect = SHOP_PIERCE_BTN_TITLE.get_rect()
shop_pierce_btn_title_rect.center = (SHOP_PIERCE_BTN_POSITION[0]+SHOP_PIERCE_BTN_DIMENSIONS[0]//2, SHOP_PIERCE_BTN_POSITION[1]-25)

#Progress Bar
PROGRESS_BAR_COORDS = (1100, 100)
PROGRESS_BAR_DIMENSIONS = (50, 600)

#Hotbox
HOTBAR_BOX_DIMENSIONS = (50, 50)
HOTBAR_BOX_Y = 725
HOTBAR_BOX_YOFFSET = -10
HOTBAR_BOX_XOFFSET = 25
HOTBAR_BOX_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 15)

SKILL_HOTBAR_BOX_DIMENSIONS = (50, 50)
SKILL_HOTBAR_BOX_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 10)

RED_EXPLOSION_RADIUS = 200

#Notifications
NOTIFICATION_COLOR = (255, 255, 0)
NOTIFICATION_OFFSET = 5
NOTIFICATION_DELAY = 30 #Frames

MANA_NOTIFICATION_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 20)
MANA_NOTIFICATION_COLOR = (255, 0, 0)
MANA_NOTIFICATION_POSITION = (MIDDLE_X, WINDOW_HEIGHT-200)


#TUTORIAL
TUTORIAL_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 18)
TUTORIAL_RECT_OFFSET = 20
TUTORIAL_TEXT_OFFSET = 30
tutorial_texts = []
tutorial_bgs = []
default_tutorial_bg = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
default_tutorial_bg.fill((0, 0, 0))
default_tutorial_bg.set_alpha(200)

TUTORIAL_NEXT_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 15)
tutorial_next_text = TUTORIAL_NEXT_FONT.render("(Click anywhere on the screen to continue)", True, (255, 215, 0))
tutorial_next_text_rect = tutorial_next_text.get_rect()
tutorial_next_text_rect.center = (950, 760) 

tutorial_icon_diameter = 150
tutorial_icon_circle_radius = tutorial_icon_diameter//2+2
tutorial_icon = pygame.image.load("resources/images/tutorial_icon.png")
tutorial_icon = pygame.transform.scale(tutorial_icon, (tutorial_icon_diameter, tutorial_icon_diameter))

TUTORIAL_OBJECTIVE_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 20)
tutorial_objective_text = TUTORIAL_OBJECTIVE_FONT.render("Objectives:", True, (0, 0, 0))
tutorial_objective_text_rect = tutorial_objective_text.get_rect()
tutorial_objective_text_rect.center = (250, 100)

TUTORIAL_HINT_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 15)
tutorial_hint_rect = pygame.rect.Rect(50, 125, 400, 200)
tutorial_hint_text_color = (0, 0, 0)
tutorial_hint_line_spacing = 30
tutorial_hints = []

TUTORIAL_BUTTON_FONT = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 30)
tutorial_w_txt = TUTORIAL_BUTTON_FONT.render("W", True, (255, 0, 0))
tutorial_s_txt = TUTORIAL_BUTTON_FONT.render("S", True, (255, 0, 0))
tutorial_a_txt = TUTORIAL_BUTTON_FONT.render("A", True, (255, 0, 0))
tutorial_d_txt = TUTORIAL_BUTTON_FONT.render("D", True, (255, 0, 0))
tutorial_w_txt_rect = tutorial_w_txt.get_rect()
tutorial_w_txt_rect.center = (600, 250)
tutorial_s_txt_rect = tutorial_s_txt.get_rect()
tutorial_s_txt_rect.center = (600, 550)
tutorial_a_txt_rect = tutorial_a_txt.get_rect()
tutorial_a_txt_rect.center = (450, 400)
tutorial_d_txt_rect = tutorial_d_txt.get_rect()
tutorial_d_txt_rect.center = (750, 400) 

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Welcome to Magic Spectrum! A game where you use magic to bring color back to the world!"
TUTORIAL_TEXT_0 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_0)
tutorial_bgs.append(None)
tutorial_hints.append(None)

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Use WASD to move Up, Left, Down, and Right, respectively"
TUTORIAL_TEXT_1 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_1)
tutorial_bgs.append(None)
tutorial_hints.append(MultilineText("Move using W, A, S, and D!", TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Nice! Now try clicking to cast a spell!"
TUTORIAL_TEXT_2 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_2)
tutorial_bgs.append(None)
tutorial_hints.append(MultilineText("Click to cast a spell toward your cursor!", TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80)
position = (275, 200)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Great Job! Every time you cast a spell, you lose mana. Make sure you keep an eye on the mana bar right above your health bar."
TUTORIAL_TEXT_3 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_3)
surface1 = pygame.Surface((1200, 635))
surface1.set_alpha(200)
surface2 = pygame.Surface((1200, 140))
surface2.set_alpha(200)
surface3 = pygame.Surface((200, 25))
surface3.set_alpha(200)
surface4 = pygame.Surface((200, 25))
surface4.set_alpha(200)
tutorial_bgs.append([[surface1, (0, 0)], [surface2, (0, 660)], [surface3, (0, 635)], [surface4, (1000, 635)]])
tutorial_hints.append(None)

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "A green enemy has now spawned on the map. Try to defeat it by casting spells!"
TUTORIAL_TEXT_4 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_4)
tutorial_bgs.append(None)
tutorial_hints.append(MultilineText("Follow the green arrow and defeat the enemy!", TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "With each enemy you defeat, you gain money and color XP (I'll explain that later). Open the shop and use your money to upgrade your damage"
TUTORIAL_TEXT_5 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_5)
surface1 = pygame.Surface((1200, 300))
surface1.set_alpha(200)
surface2 = pygame.Surface((1200, 425))
surface2.set_alpha(200)
surface3 = pygame.Surface((25, 75))
surface3.set_alpha(200)
surface4 = pygame.Surface((1025, 75))
surface4.set_alpha(200)
tutorial_bgs.append([[surface1, (0, 0)], [surface2, (0, 375)], [surface3, (0, 300)], [surface4, (175, 300)]])
tutorial_hints.append(MultilineText('Open the shop and buy the "damage" upgrade!', TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Now we will start the next round. The beginning of each round spawns new enemies. Try to make it past round 2!"
TUTORIAL_TEXT_6 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_6)
tutorial_bgs.append(None)
tutorial_hints.append(MultilineText("Make it past round 2", TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Nice! If you noticed, color XP fills the bar on the right side of your screen. When you fill it up, you will unlock a new spell and upgrades in the shop!"
TUTORIAL_TEXT_7 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_7)
surface1 = pygame.Surface((1200, 100))
surface1.set_alpha(200)
surface2 = pygame.Surface((1200, 100))
surface2.set_alpha(200)
surface3 = pygame.Surface((1100, 600))
surface3.set_alpha(200)
surface4 = pygame.Surface((50, 600))
surface4.set_alpha(200)
tutorial_bgs.append([[surface1, (0, 0)], [surface2, (0, 700)], [surface3, (0, 100)], [surface4, (1150, 100)]])
tutorial_hints.append(None)

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Get more color XP to fill up the bar!"
TUTORIAL_TEXT_8 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_8)
tutorial_bgs.append(None)
tutorial_hints.append(MultilineText("Defeat enough enemies to fill the color XP bar", TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "You unlocked the poison spell, which deals a percentage of the enemy's health as Damage over Time! You can switch between spells using the number keys or scroll wheel."
TUTORIAL_TEXT_9 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_9)
surface1 = pygame.Surface((1200, 725))
surface1.set_alpha(200)
surface2 = pygame.Surface((1200, 25))
surface2.set_alpha(200)
surface3 = pygame.Surface((637-25, 50))
surface3.set_alpha(200)
surface4 = pygame.Surface((513+25, 50))
surface4.set_alpha(200)
tutorial_bgs.append([[surface1, (0, 0)], [surface2, (0, 775)], [surface3, (0, 725)], [surface4, (687-25, 725)]])
tutorial_hints.append(None)

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "You also unlocked new upgrades in the shop, check them out later"
TUTORIAL_TEXT_10 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_10)
surface1 = pygame.Surface((1200, 300))
surface1.set_alpha(200)
surface2 = pygame.Surface((1200, 425))
surface2.set_alpha(200)
surface3 = pygame.Surface((25, 75))
surface3.set_alpha(200)
surface4 = pygame.Surface((1025, 75))
surface4.set_alpha(200)
tutorial_bgs.append([[surface1, (0, 0)], [surface2, (0, 375)], [surface3, (0, 300)], [surface4, (175, 300)]])
tutorial_hints.append(None)

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Now, a new type of enemy has spawned: the red enemy. This enemy is tankier and deals more damage. Try to defeat it with your new spell!"
TUTORIAL_TEXT_11 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_11)
tutorial_bgs.append(None)
tutorial_hints.append(MultilineText("Defeat the red enemies", TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "You have unlocked the explosion spell! This spell deals damage in an AOE"
TUTORIAL_TEXT_12 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_12)
surface1 = pygame.Surface((1200, 725))
surface1.set_alpha(200)
surface2 = pygame.Surface((1200, 25))
surface2.set_alpha(200)
surface3 = pygame.Surface((650, 50))
surface3.set_alpha(200)
surface4 = pygame.Surface((500, 50))
surface4.set_alpha(200)
tutorial_bgs.append([[surface1, (0, 0)], [surface2, (0, 775)], [surface3, (0, 725)], [surface4, (700, 725)]])
tutorial_hints.append(None)

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "If you ever get confused about what certain spells do, check the spell info button on the left of your screen"
TUTORIAL_TEXT_13 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_13)
surface1 = pygame.Surface((1200, 385))
surface1.set_alpha(200)
surface2 = pygame.Surface((1200, 365))
surface2.set_alpha(200)
surface3 = pygame.Surface((25, 50))
surface3.set_alpha(200)
surface4 = pygame.Surface((1075, 50))
surface4.set_alpha(200)
tutorial_bgs.append([[surface1, (0, 0)], [surface2, (0, 435)], [surface3, (0, 385)], [surface4, (125, 385)]])
INFO_BUTTON_COORDS = (25, 385)
INFO_BUTTON_DIMENSIONS = (100, 50)
tutorial_hints.append(None)

dimensions = (800, 80)
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Another enemy type has spawned, the blue enemy. This enemy is much faster."
TUTORIAL_TEXT_14 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_14)
tutorial_bgs.append(None)
tutorial_hints.append(MultilineText("Defeat the blue enemy", TUTORIAL_HINT_FONT, tutorial_hint_text_color, tutorial_hint_rect, tutorial_hint_line_spacing, "center", "top"))

dimensions = (800, 80) 
position = (275, 600)
rect = pygame.Rect(position[0], position[1], dimensions[0], dimensions[1])
text = "Congratulations! You have completed the tutorial and now know to play Magic Spectrum! Have fun and good luck!"
TUTORIAL_TEXT_15 = MultilineText(text, TUTORIAL_FONT, (0, 0, 0), rect, TUTORIAL_TEXT_OFFSET, "center", "center")
tutorial_texts.append(TUTORIAL_TEXT_15)
tutorial_bgs.append(None)
tutorial_hints.append(None)


#General
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Magic Spectrum')


INDICATOR_DISTANCE = 150
INDICATOR_DEAC_DISTANCE = 650
INDICATOR_DIMENSIONS = (32, 64)

def updateIndicator(player_x, player_y, enemies):
  indicator_arrow = pygame.image.load("resources/images/green_arrow.png")
  angle = -1
  x_coord = 0
  y_coord = 0

  try:
    closest_dist = math.dist((enemies[0].x+enemies[0].width//2, enemies[0].y+enemies[0].height//2), (player_x, player_y))
    closest_enemy_index = 0
    for i, enemy in enumerate(enemies):
      dist = math.dist((enemy.x+enemy.width//2, enemy.y+enemy.height//2), (player_x, player_y))
      if dist < closest_dist:
        closest_dist = dist
        closest_enemy_index = i
    
    if enemies[closest_enemy_index].type == "red":
      indicator_arrow = pygame.image.load("resources/images/red_arrow.png")
    elif enemies[closest_enemy_index].type == "blue":
      indicator_arrow = pygame.image.load("resources/images/blue_arrow.png")
    elif enemies[closest_enemy_index].type == "yellow":
      indicator_arrow = pygame.image.load("resources/images/yellow_arrow.png")
    elif enemies[closest_enemy_index].type == "rainbow":
      indicator_arrow = pygame.image.load("resources/images/rainbow_arrow.png")
    indicator_arrow = pygame.transform.scale(indicator_arrow, INDICATOR_DIMENSIONS)
    
    if closest_dist < INDICATOR_DEAC_DISTANCE:
      return indicator_arrow, angle, x_coord, y_coord
    else:
      enemy_x, enemy_y = enemies[closest_enemy_index].x+enemies[closest_enemy_index].width//2, enemies[closest_enemy_index].y+enemies[closest_enemy_index].height//2

      x_dist, y_dist = enemy_x-player_x, enemy_y-player_y

      interval = closest_dist/INDICATOR_DISTANCE
      x_coord, y_coord = round(player_x+x_dist/interval-INDICATOR_DIMENSIONS[0]//2), round(player_y+y_dist/interval-INDICATOR_DIMENSIONS[1]//2)

      x_negative, y_negative = False, False
      if x_dist < 0:
        x_negative = True
      if y_dist < 0:
        y_negative = True
      x_dist, y_dist = abs(x_dist), abs(y_dist)

      angle = round(math.degrees(math.atan(y_dist/x_dist)))
      if x_negative and y_negative:
        angle = 180 - angle
      elif x_negative:
        angle += 180
      elif not y_negative:
        angle = 360 - angle
      indicator_arrow = pygame.transform.rotate(indicator_arrow, angle-90)


      return indicator_arrow, angle, x_coord, y_coord
  except:
    return indicator_arrow, angle, x_coord, y_coord





class GameScreen:
  #Initializes all of the variables that are needed for the screen to work
  def __init__(self, difficulty):
    
    self.creative = False
    if difficulty == "creative":
      self.creative = True

    #VARIABLES
    self.background_x = 0
    self.background_y = 0

    self.player_x = MIDDLE_X
    self.player_y = MIDDLE_Y

    if self.creative:
      self.money = 100000000
    else:
      self.money = 0
    self.money_multiplyer = 1

    self.hitboxes = settings["hitboxes"]
    self.camera_shake = settings["camera_shake"]

    self.speed_value = 4
    self.speed = self.speed_value
    self.speed_accel = 0
    self.speed_accel_interval = 0.1

    self.damage = 10
    
    self.pierce = 1

    self.settings_indicator_arrow_on = settings["ne"]
    self.indicator_arrow_on = True

    self.summon_enemies = []

    self.in_tutorial = False
    self.tutorial_index = 0
    self.tutorial_wasd_pressed = [0, 0, 0, 0]
    self.tutorial_frames = 0
    self.tutorial_pause_length = 60 #frames
    self.tutorial_next_text_shown = True
    
    #Mana Settings/Variables
    self.max_mana = 100
    self.mana = self.max_mana
    self.mana_regen_rate = 0.00125
    self.not_enough_mana = False
    self.not_enough_mana_frames = 0
    self.not_enough_mana_time = 60 #Frames

    #Dash Settings/Variables
    self.dash = 0
    self.dash_cooldown_time = 120 #frames
    self.dash_cooldown_frames = 0
    self.dashing = False
    self.dashing_frames = 0

    #Cooldown Settings/Variables
    self.cooldown_timer = 60 #frames
    self.cooldown = 0

    self.reload = False

    self.in_shop = False
    self.in_info = False
    self.info_entry = 0

    #Shop Buttons Activation
    self.green_buttons = self.creative
    self.red_buttons = self.creative
    self.blue_buttons = self.creative
    self.yellow_buttons = self.creative

    self.switch_map = False
    self.prog_color = (0, 128, 82)

    self.difficulty = difficulty

    self.draw_red_explosion = []
    self.red_explosion_frames = []

    self.charging_purple = False

    self.camera_x_change = 0
    self.camera_y_change = 0

    self.spawn_enemies = True



    self.reload_mults = [1, 1.5, 5, 2, 0.25, 20]

    #Creative Differentiation
    if self.creative:
      self.bullet_hotbar = ["black", "green", "red", "blue", "yellow", "rainbow"]
      self.bullet_cooldowns = [self.cooldown_timer*1, self.cooldown_timer*1.5, self.cooldown_timer*5, self.cooldown_timer*2, self.cooldown_timer*0.25, self.cooldown_timer*20]
      self.bullet_reloads = [0, 0, 0, 0, 0, 0]
      self.bullet_available = [True, True, True, True, True, True]
    else:
      self.bullet_hotbar = ["black"]
      self.bullet_cooldowns = [self.cooldown_timer*1]
      self.bullet_reloads = [0]
      self.bullet_available = [True]
    self.bullet_index = 0

    self.skill_hotbar = []

    #Settings Button
    self.SETTINGS_BUTTON_POS = (25, 725)
    self.SETTINGS_BUTTON_DIMENSIONS = (50, 50)
    self.SETTINGS_BUTTON_COLOR = (255, 255, 255)
    self.SETTINGS_BUTTON_HCOLOR = (220, 220, 220)
    self.SETTINGS_BUTTON_PCOLOR = (180, 180, 180)
    self.settings_button = Button(self.SETTINGS_BUTTON_POS, self.SETTINGS_BUTTON_DIMENSIONS, self.SETTINGS_BUTTON_COLOR)
    self.settings_button.image("resources/images/settings_icon.png")

    #HP
    self.max_health = 100
    self.health = 100
    self.healthbar_bg_rect = pygame.Rect(HEALTHBAR_X, HEALTHBAR_Y, HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT)
    self.healthbar_rect = pygame.Rect(HEALTHBAR_X, HEALTHBAR_Y, HEALTHBAR_WIDTH, HEALTHBAR_HEIGHT)

    #Hitboxes/Damage
    self.invincible = False
    self.invincible_frames = 0

    #Enemies killed
    self.green_killed = 0
    self.red_killed = 0
    self.blue_killed = 0
    self.yellow_killed = 0
    self.rainbow_killed = 0

    #Map Progress Bar
    self.progress_bar = pygame.Rect(PROGRESS_BAR_COORDS[0], PROGRESS_BAR_COORDS[1], PROGRESS_BAR_DIMENSIONS[0], PROGRESS_BAR_DIMENSIONS[1])
    self.colored_progress_bar = pygame.Rect(PROGRESS_BAR_COORDS[0], PROGRESS_BAR_COORDS[1], PROGRESS_BAR_DIMENSIONS[0], PROGRESS_BAR_DIMENSIONS[1])

    #STATE
    self.running = False
    
    #COLORS
    self.color_bg = COLOR_BACKGROUND

    #BACKGROUND
    #self.background = pygame.Rect(self.background_x, self.background_y, BACKGROUND_WIDTH, BACKGROUND_HEIGHT)
    self.map = "resources/images/map_white.png"
    self.background = pygame.image.load(self.map)
    self.background = pygame.transform.scale(self.background, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))

    #CURSOR
    self.cursor = pygame.image.load('resources/images/cursor_sprite.png').convert_alpha()
    self.cursor = pygame.transform.scale(self.cursor, (CURSOR_WIDTH, CURSOR_HEIGHT))
    self.cursor_x = 0
    self.cursor_y = 0

    #COOLDOWN RECT
    self.cooldown_rect = pygame.Rect(0, 0, COOLDOWN_RECT_DIMENSIONS[0], COOLDOWN_RECT_DIMENSIONS[1])
    self.cooldown_rect_bg = pygame.Rect(0, 0, COOLDOWN_RECT_DIMENSIONS[0], COOLDOWN_RECT_DIMENSIONS[1])

    #MANA BAR
    self.mana_background_bar = pygame.Rect(MANA_BAR_COORDS[0], MANA_BAR_COORDS[1], MANA_BAR_DIMENSIONS[0], MANA_BAR_DIMENSIONS[1])
    self.mana_bar = pygame.Rect(MANA_BAR_COORDS[0], MANA_BAR_COORDS[1], 0, MANA_BAR_DIMENSIONS[1])

    #PLAYER
    self.player_frame = 0
    self.player = pygame.image.load('resources/images/player_frame0.png').convert_alpha()
    self.player = pygame.transform.scale(self.player, (PLAYER_WIDTH, PLAYER_HEIGHT))
    self.player_frames = 0
    self.player_frame_reversed = False

    #BULLETS
    self.bullets = []


    #USERINPUTS
    self.mouseIsDown = False
    self.mouseUp = False
    self.mouseDown = False
    self.mousePos = None

    self.w_down = False
    self.s_down = False
    self.a_down = False
    self.d_down = False



    #ENEMIES
    self.enemies = []

    #INFO BUTTON
    self.info_button = Button((INFO_BUTTON_COORDS[0], INFO_BUTTON_COORDS[1]), (INFO_BUTTON_DIMENSIONS[0], INFO_BUTTON_DIMENSIONS[1]), (INFO_BUTTON_COLOR))
    self.info_button.add_border(INFO_BUTTON_BORDER_WIDTH, INFO_BUTTON_BORDER_COLOR)
    self.info_button.add_text(INFO_BUTTON_FONT, "Spell info", INFO_BUTTON_TEXT_COLOR, INFO_BUTTON_TEXT_YOFFSET)

    #Spell Info Screen
    self.info_bg_rect = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    self.info_bg_rect.set_alpha(INFO_BG_RECT_ALPHA)
    self.info_bg_rect.fill((0, 0, 0))

    self.info_back = pygame.image.load("resources/images/info_background.png")
    self.info_back = pygame.transform.scale(self.info_back, (WINDOW_WIDTH-INFO_BG_OFFSET*2, WINDOW_HEIGHT-INFO_BG_OFFSET*2))
    #self.info_back = pygame.Rect(INFO_BG_OFFSET, INFO_BG_OFFSET, WINDOW_WIDTH-INFO_BG_OFFSET*2, WINDOW_HEIGHT-INFO_BG_OFFSET*2)

    self.info_close_btn = Button(INFO_CLOSE_BUTTON_POSITION, INFO_CLOSE_BUTTON_DIMENSIONS, (255, 219, 171))
    self.info_close_btn.add_text(INFO_CLOSE_BUTTON_FONT, "X", (0, 0, 0), 3)

    self.info_left_button = Button(INFO_LEFT_BUTTON_COORDS, INFO_LEFT_BUTTON_DIMENSIONS, INFO_DBUTTON_COLOR)
    self.info_left_button.add_text(INFO_DBUTTON_FONT, "<", INFO_DBUTTON_TEXT_COLOR)

    self.info_right_button = Button(INFO_RIGHT_BUTTON_COORDS, INFO_RIGHT_BUTTON_DIMENSIONS, INFO_DBUTTON_COLOR)
    self.info_right_button.add_text(INFO_DBUTTON_FONT, ">", INFO_DBUTTON_TEXT_COLOR)

    #SHOP BUTTON
    self.shop_button = Button((SHOP_BUTTON_X, SHOP_BUTTON_Y), (SHOP_BUTTON_WIDTH, SHOP_BUTTON_HEIGHT), (SHOP_BUTTON_COLOR))
    self.shop_button.add_border(SHOP_BUTTON_BORDER_WIDTH, SHOP_BUTTON_BORDER_COLOR)
    self.shop_button.add_text(SHOP_BUTTON_FONT, "Shop", SHOP_BUTTON_TEXT_COLOR, SHOP_BUTTON_TEXT_YOFFSET)
    

    #SHOP SCREEN
    self.shop_bg_rect = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
    self.shop_bg_rect.set_alpha(SHOP_BG_RECT_ALPHA)
    self.shop_bg_rect.fill((0, 0, 0))

    self.shop_back = pygame.image.load("resources/images/shop_background.png")
    self.shop_back = pygame.transform.scale(self.shop_back, (WINDOW_WIDTH-SHOP_BG_OFFSET*2, WINDOW_HEIGHT-SHOP_BG_OFFSET*2))


    #Stats (first is price, second is damage)
    self.damage_stats = [15, 30, 50, 75, 200, 500, 1000]
    self.damage_price = [25, 100, 250, 500, 2000, 10000, 50000]

    self.money_stats = [1.25, 1.5, 2, 3, 5, 10]
    self.money_price = [100, 500, 1500, 6000, 20000, 100000]

    self.grn_stats = [150, 200, 300, 400, 500, 750, 1000]
    self.grn_price = [50, 200, 500, 2000, 5000, 10000, 25000]

    self.dash_stats = [5, 7, 10, 15, 20, 25, 30]
    self.dash_price = [200, 800, 1750, 5000, 12500, 25000, 75000]

    self.atkspd_stats = [50, 40, 30, 20, 10, 5, 3]
    self.atkspd_price = [100, 1250, 5000, 10000, 20000, 50000, 100000]

    self.mana_stats = [150, 200, 300, 500, 750, 1000]
    self.mana_price = [500, 2000, 10000, 25000, 75000, 200000]

    self.spd_stats = [5, 6, 7, 8, 9, 10]
    self.spd_price = [500, 1250, 5000, 15000, 40000, 65000]

    self.pierce_stats = [2, 3, 4, 5, 6, 7]
    self.pierce_price = [1000, 2500, 5000, 12500, 25000, 50000]
    
    


    #Shop Close Button Init
    self.shop_close_btn = Button(SHOP_CLOSE_BUTTON_POSITION, SHOP_CLOSE_BUTTON_DIMENSIONS, (163, 60, 26))
    self.shop_close_btn.add_border(8, (160, 25, 0))
    self.shop_close_btn.add_text(SHOP_CLOSE_BUTTON_FONT, "X", (0, 0, 0), 3)
    
    #Shop Damage Button Init
    self.shop_damage_btn = Button(SHOP_DAMAGE_BTN_POSITION, SHOP_DAMAGE_BTN_DIMENSIONS, SHOP_DAMAGE_BTN_COLOR)
    self.shop_damage_btn.add_border(5, (0, 0, 0))
    self.shop_damage_btn.add_text(SHOP_ITEM_FONT, f"${self.damage_price[0]}", (0, 255, 0), 3)
    self.shop_damage_btn_sub = SHOP_SUB_FONT.render(f"{self.damage} -> {self.damage_stats[0]}", True, (0, 0, 0))
    self.shop_damage_btn_sub_rect = self.shop_damage_btn_sub.get_rect()
    self.shop_damage_btn_sub_rect.center = (SHOP_DAMAGE_BTN_POSITION[0]+SHOP_DAMAGE_BTN_DIMENSIONS[0]//2, SHOP_DAMAGE_BTN_POSITION[1]+SHOP_DAMAGE_BTN_DIMENSIONS[1]+25)

    #Shop Money Button Init
    self.shop_money_btn = Button(SHOP_MONEY_BTN_POSITION, SHOP_MONEY_BTN_DIMENSIONS, SHOP_MONEY_BTN_COLOR)
    self.shop_money_btn.add_border(5, (0, 0, 0))
    self.shop_money_btn.add_text(SHOP_ITEM_FONT, f"${self.money_price[0]}", (0, 255, 0), 3)
    self.shop_money_btn_sub = SHOP_SUB_FONT.render(f"{self.money_multiplyer} -> {self.money_stats[0]}", True, (0, 0, 0))
    self.shop_money_btn_sub_rect = self.shop_money_btn_sub.get_rect()
    self.shop_money_btn_sub_rect.center = (SHOP_MONEY_BTN_POSITION[0]+SHOP_MONEY_BTN_DIMENSIONS[0]//2, SHOP_MONEY_BTN_POSITION[1]+SHOP_MONEY_BTN_DIMENSIONS[1]+25)
    
    #Shop Health Button Init
    self.shop_grn_btn = Button(SHOP_GRN_BTN_POSITION, SHOP_GRN_BTN_DIMENSIONS, SHOP_GRN_BTN_COLOR)
    self.shop_grn_btn.add_border(5, (0, 0, 0))
    self.shop_grn_btn.add_text(SHOP_ITEM_FONT, f"${self.grn_price[0]}", (0, 255, 0), 3)
    self.shop_grn_btn_sub = SHOP_SUB_FONT.render(f"{self.max_health} -> {self.grn_stats[0]}", True, (0, 0, 0))
    self.shop_grn_btn_sub_rect = self.shop_grn_btn_sub.get_rect()
    self.shop_grn_btn_sub_rect.center = (SHOP_GRN_BTN_POSITION[0]+SHOP_GRN_BTN_DIMENSIONS[0]//2, SHOP_GRN_BTN_POSITION[1]+SHOP_GRN_BTN_DIMENSIONS[1]+25)

    #Shop Dash Button Init
    self.shop_dash_btn = Button(SHOP_DASH_BTN_POSITION, SHOP_DASH_BTN_DIMENSIONS, SHOP_DASH_BTN_COLOR)
    self.shop_dash_btn.add_border(5, (0, 0, 0))
    self.shop_dash_btn.add_text(SHOP_ITEM_FONT, f"${self.dash_price[0]}", (0, 255, 0), 3)
    self.shop_dash_btn_sub = SHOP_SUB_FONT.render(f"{self.dash} -> {self.dash_stats[0]}", True, (0, 0, 0))
    self.shop_dash_btn_sub_rect = self.shop_dash_btn_sub.get_rect()
    self.shop_dash_btn_sub_rect.center = (SHOP_DASH_BTN_POSITION[0]+SHOP_DASH_BTN_DIMENSIONS[0]//2, SHOP_DASH_BTN_POSITION[1]+SHOP_DASH_BTN_DIMENSIONS[1]+25)

    #Shop Atkspd Button Init
    self.shop_atkspd_btn = Button(SHOP_ATKSPD_BTN_POSITION, SHOP_ATKSPD_BTN_DIMENSIONS, SHOP_ATKSPD_BTN_COLOR)
    self.shop_atkspd_btn.add_border(5, (0, 0, 0))
    self.shop_atkspd_btn.add_text(SHOP_ITEM_FONT, f"${self.atkspd_price[0]}", (0, 255, 0), 3)
    self.shop_atkspd_btn_sub = SHOP_SUB_FONT.render(f"{self.cooldown_timer} -> {self.atkspd_stats[0]}", True, (0, 0, 0))
    self.shop_atkspd_btn_sub_rect = self.shop_atkspd_btn_sub.get_rect()
    self.shop_atkspd_btn_sub_rect.center = (SHOP_ATKSPD_BTN_POSITION[0]+SHOP_ATKSPD_BTN_DIMENSIONS[0]//2, SHOP_ATKSPD_BTN_POSITION[1]+SHOP_ATKSPD_BTN_DIMENSIONS[1]+25)

    #Shop Mana Button Init
    self.shop_mana_btn = Button(SHOP_MANA_BTN_POSITION, SHOP_MANA_BTN_DIMENSIONS, SHOP_MANA_BTN_COLOR)
    self.shop_mana_btn.add_border(5, (0, 0, 0))
    self.shop_mana_btn.add_text(SHOP_ITEM_FONT, f"${self.mana_price[0]}", (0, 255, 0), 3)
    self.shop_mana_btn_sub = SHOP_SUB_FONT.render(f"{self.max_mana} -> {self.mana_stats[0]}", True, (0, 0, 0))
    self.shop_mana_btn_sub_rect = self.shop_mana_btn_sub.get_rect()
    self.shop_mana_btn_sub_rect.center = (SHOP_MANA_BTN_POSITION[0]+SHOP_MANA_BTN_DIMENSIONS[0]//2, SHOP_MANA_BTN_POSITION[1]+SHOP_MANA_BTN_DIMENSIONS[1]+25)

    #Shop Speed Button Init
    self.shop_spd_btn = Button(SHOP_SPD_BTN_POSITION, SHOP_SPD_BTN_DIMENSIONS, SHOP_SPD_BTN_COLOR)
    self.shop_spd_btn.add_border(5, (0, 0, 0))
    self.shop_spd_btn.add_text(SHOP_ITEM_FONT, f"${self.spd_price[0]}", (0, 255, 0), 3)
    self.shop_spd_btn_sub = SHOP_SUB_FONT.render(f"{self.speed_value} -> {self.spd_stats[0]}", True, (0, 0, 0))
    self.shop_spd_btn_sub_rect = self.shop_spd_btn_sub.get_rect()
    self.shop_spd_btn_sub_rect.center = (SHOP_SPD_BTN_POSITION[0]+SHOP_SPD_BTN_DIMENSIONS[0]//2, SHOP_SPD_BTN_POSITION[1]+SHOP_SPD_BTN_DIMENSIONS[1]+25)

    #Shop Pierce Button Init
    self.shop_pierce_btn = Button(SHOP_PIERCE_BTN_POSITION, SHOP_PIERCE_BTN_DIMENSIONS, SHOP_PIERCE_BTN_COLOR)
    self.shop_pierce_btn.add_border(5, (0, 0, 0))
    self.shop_pierce_btn.add_text(SHOP_ITEM_FONT, f"${self.pierce_price[0]}", (0, 255, 0), 3)
    self.shop_pierce_btn_sub = SHOP_SUB_FONT.render(f"{self.pierce} -> {self.pierce_stats[0]}", True, (0, 0, 0))
    self.shop_pierce_btn_sub_rect = self.shop_pierce_btn_sub.get_rect()
    self.shop_pierce_btn_sub_rect.center = (SHOP_PIERCE_BTN_POSITION[0]+SHOP_PIERCE_BTN_DIMENSIONS[0]//2, SHOP_PIERCE_BTN_POSITION[1]+SHOP_PIERCE_BTN_DIMENSIONS[1]+25)


    #Creative Spawning Enemies Text
    text = "SPAWNING ENEMIES\n\ng = spawn Green Enemy\no = spawn Red Enemy\nb = spawn Blue Enemy\ny = spawn Yellow Enemy\nt = spawn Rainbow Enemy\nshift+key = spawn Boss Enemy"
    font = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 8)
    rect = pygame.Rect(25, 325, 200, 400)
    self.spawning_enemies_text = MultilineText(text, font, (0, 0, 0), rect, 15, "left", "center")


    


    #Rounds/Difficulty
    self.rounds = []
    #Easy
    if difficulty == "easy":
      self.GREEN_NEEDED = 7
      self.RED_NEEDED = 7
      self.BLUE_NEEDED = 7
      self.YELLOW_NEEDED = 5
      self.RAINBOW_NEEDED = 5
      self.difficulty_money_multiplyer = 4
      self.rounds.append({"green":1}) #ROUND 1
      self.rounds.append({"green":2}) #ROUND 2
      self.rounds.append({"green":3}) #ROUND 3
      self.rounds.append({"green":4}) #ROUND 4
      self.rounds.append({"red":1}) #ROUND 5
      self.rounds.append({"red":2}) #ROUND 6
      self.rounds.append({"red":1, "green":2}) #7
      self.rounds.append({"red":2, "green":3}) #Round 8
      self.rounds.append({"red":4}) #Round 9
      self.rounds.append({"blue":1}) #ROUND 10
      self.rounds.append({"blue":2}) #ROUND 11
      self.rounds.append({"blue":1, "red":1, "green":3}) #ROUND 12
      self.rounds.append({"blue":1, "red":2, "green":4}) #ROUND 13
      self.rounds.append({"blue":2}) #ROUND 14
      self.rounds.append({"blue":2, "red":3, "green":4}) #ROUND 15
      self.rounds.append({"yellow":1}) #ROUND 15
      self.rounds.append({"yellow":2}) #16
      self.rounds.append({"yellow":1, "blue":1}) #17
      self.rounds.append({"yellow":1, "blue":2, "red":2, "green":2}) #18
      self.rounds.append({"yellow":2, "blue":2, "red":1, "green":3}) #19
      self.rounds.append({"rainbow":1}) #20
      self.rounds.append({"rainbow":1}) #21
      self.rounds.append({"rainbow":2}) #22
      self.rounds.append({"rainbow":1, "yellow":3, "blue":2}) #23
      self.rounds.append({"rainbow":3}) #24
      self.rounds.append({"rainbow":3, "yellow":3, "blue":2}) #25
    #Medium
    elif difficulty == "medium":
      self.GREEN_NEEDED = 15
      self.RED_NEEDED = 15
      self.BLUE_NEEDED = 15
      self.YELLOW_NEEDED = 10
      self.RAINBOW_NEEDED = 10
      self.difficulty_money_multiplyer = 1
      self.rounds.append({"green":1}) #ROUND 1
      self.rounds.append({"green":3}) #ROUND 2
      self.rounds.append({"green":5}) #ROUND 3
      self.rounds.append({"green":7}) #ROUND 4
      self.rounds.append({"red":1}) #ROUND 5
      self.rounds.append({"red":3}) #ROUND 6
      self.rounds.append({"red":1, "green":3}) #7
      self.rounds.append({"red":3, "green":5}) #Round 8
      self.rounds.append({"red":8}) #Round 9
      self.rounds.append({"blue":1}) #ROUND 10
      self.rounds.append({"blue":3}) #ROUND 11
      self.rounds.append({"blue":1, "red":2, "green":5}) #ROUND 12
      self.rounds.append({"blue":2, "red":4, "green":7}) #ROUND 13
      self.rounds.append({"blue":4}) #ROUND 14
      self.rounds.append({"blue":4, "red":5, "green":7}) #ROUND 15
      self.rounds.append({"yellow":1}) #ROUND 15
      self.rounds.append({"yellow":3}) #16
      self.rounds.append({"yellow":2, "blue":2}) #17
      self.rounds.append({"yellow":2, "blue":3, "red":3, "green":3}) #18
      self.rounds.append({"yellow":4, "blue":3, "red":2, "green":5}) #19
      self.rounds.append({"rainbow":1}) #20
      self.rounds.append({"rainbow":2}) #21
      self.rounds.append({"rainbow":4}) #22
      self.rounds.append({"rainbow":2, "yellow":5, "blue":3}) #23
      self.rounds.append({"rainbow":6}) #24
      self.rounds.append({"rainbow":5, "yellow":5, "blue":3}) #25
    #Hard
    elif difficulty == "hard":
      self.GREEN_NEEDED = 30
      self.RED_NEEDED = 30
      self.BLUE_NEEDED = 30
      self.YELLOW_NEEDED = 20
      self.RAINBOW_NEEDED = 20
      self.difficulty_money_multiplyer = 1
      self.rounds.append({"green":2}) #ROUND 1
      self.rounds.append({"green":6}) #ROUND 2
      self.rounds.append({"green":10}) #ROUND 3
      self.rounds.append({"green":14}) #ROUND 4
      self.rounds.append({"red":2}) #ROUND 5
      self.rounds.append({"red":6}) #ROUND 6
      self.rounds.append({"red":2, "green":6}) #7
      self.rounds.append({"red":6, "green":10}) #Round 8
      self.rounds.append({"red":16}) #Round 9
      self.rounds.append({"blue":2}) #ROUND 10
      self.rounds.append({"blue":6}) #ROUND 11
      self.rounds.append({"blue":2, "red":4, "green":10}) #ROUND 12
      self.rounds.append({"blue":4, "red":8, "green":14}) #ROUND 13
      self.rounds.append({"blue":8}) #ROUND 14
      self.rounds.append({"blue":8, "red":10, "green":14}) #ROUND 15
      self.rounds.append({"yellow":2}) #ROUND 15
      self.rounds.append({"yellow":6}) #16
      self.rounds.append({"yellow":4, "blue":4}) #17
      self.rounds.append({"yellow":4, "blue":6, "red":6, "green":6}) #18
      self.rounds.append({"yellow":8, "blue":6, "red":4, "green":10}) #19
      self.rounds.append({"rainbow":2}) #20
      self.rounds.append({"rainbow":4}) #21
      self.rounds.append({"rainbow":8}) #22
      self.rounds.append({"rainbow":4, "yellow":10, "blue":6}) #23
      self.rounds.append({"rainbow":12}) #24
      self.rounds.append({"rainbow":10, "yellow":10, "blue":6}) #25
    #Creative
    elif difficulty == "creative":
      self.GREEN_NEEDED = 5
      self.RED_NEEDED = 5
      self.BLUE_NEEDED = 5
      self.YELLOW_NEEDED = 5
      self.RAINBOW_NEEDED = 5
      self.difficulty_money_multiplyer = 1
      self.rounds.append({"green":3}) #ROUND 1
      self.rounds.append({"red":3})
      self.rounds.append({"blue":3})
      self.rounds.append({"yellow":3})
      self.rounds.append({"rainbow":3})
      self.rounds.append({"green_boss":1})
      self.rounds.append({"red_boss":1})
      self.rounds.append({"blue_boss":1})
      self.rounds.append({"yellow_boss":1})
      self.rounds.append({"rainbow_boss":1})
      self.rounds.append({"green":5})
      self.rounds.append({"red":5})
      self.rounds.append({"blue":5})
      self.rounds.append({"yellow":5})
      self.rounds.append({"rainbow":5})
      self.rounds.append({"green":1, "red":1, "blue":1, "yellow":1, "rainbow":1})
      self.rounds.append({"green":2, "red":2, "blue":2, "yellow":2, "rainbow":2})
      self.rounds.append({"green_boss":1, "red_boss":1, "blue_boss":1, "yellow_boss":1, "rainbow_boss":1})
    #Tutorial
    elif difficulty == "tutorial":
      self.money = 15
      self.GREEN_NEEDED = 6
      self.RED_NEEDED = 2
      self.BLUE_NEEDED = 1
      self.YELLOW_NEEDED = 1
      self.RAINBOW_NEEDED = 1
      self.difficulty_money_multiplyer = 1
      self.rounds.append({"green":1}) #ROUND 1
      self.rounds.append({"green":2})
      self.rounds.append({"green":3})
      self.rounds.append({"red":2})
      self.rounds.append({"blue":1})
      self.rounds.append({"blue":3})
      

    self.health = self.max_health


    #Rounds
    self.next_round = True
    self.round = 0
    

    #Notifications
    self.notification_frames = 0
    if not self.creative:
      self.shop_notifications_on = False
      self.info_notifications_on = False
    else:
      self.shop_notifications_on = True
      self.info_notifications_on = True
    self.shop_notification = pygame.Rect(self.shop_button.x-NOTIFICATION_OFFSET, self.shop_button.y-NOTIFICATION_OFFSET, self.shop_button.width+NOTIFICATION_OFFSET*2, self.shop_button.height+NOTIFICATION_OFFSET*2)
    self.info_notification = pygame.Rect(self.info_button.x-NOTIFICATION_OFFSET, self.info_button.y-NOTIFICATION_OFFSET, self.info_button.width+NOTIFICATION_OFFSET*2, self.info_button.height+NOTIFICATION_OFFSET*2)


    #Escape Text
    self.escape_text_font = pygame.font.Font("resources/fonts/fff-forward.regular.ttf", 10)
    self.escape_text = self.escape_text_font.render("Press ESC to return to Home Screen", True, (0, 0, 0))
    self.escape_text_rect = self.escape_text.get_rect() 
    self.escape_text_rect.center = (150, 25)
    




    
  
    self.on_shift = False

  def run(self, events):
    """GETS USER INPUTS"""
    self.mouseDown = False
    self.mouseUp = False
    self.mousePos = pygame.mouse.get_pos()
    self.shift_pressed = False
    for event in events:
      if event.type == QUIT :
        pygame.quit()
        sys.exit()
      if event.type == MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
          self.mouseIsDown = True
          self.mouseDown = True
        if event.button == 4:
          self.bullet_index += 1
          if self.bullet_index >= len(self.bullet_hotbar):
            self.bullet_index = len(self.bullet_hotbar)-1
        if event.button == 5:
          self.bullet_index -= 1
          if self.bullet_index < 0:
            self.bullet_index = 0
      if event.type == MOUSEBUTTONUP:
        self.mouseIsDown = False
        self.mouseUp = True
      if event.type == KEYUP:
        if pygame.key.get_pressed()[pygame.K_a] != True and pygame.key.get_pressed()[pygame.K_d] != True and pygame.key.get_pressed()[pygame.K_s] != True and pygame.key.get_pressed()[pygame.K_w] != True:
          self.speed_accel = 0
        if event.key == K_LSHIFT or event.key == K_RSHIFT:
          self.shift_pressed = False
      if event.type == KEYDOWN:
        if event.key == K_w:
          self.w_down = True
          self.s_down = False
          self.speed_accel += self.speed_accel_interval
        elif event.key == K_s:
          self.s_down = True
          self.w_down = False
          self.speed_accel += self.speed_accel_interval
        elif event.key == K_a:
          self.a_down = True
          self.d_down = False
          self.speed_accel += self.speed_accel_interval
        elif event.key == K_d:
          self.d_down = True
          self.a_down = False
          self.speed_accel += self.speed_accel_interval
        elif event.key == K_ESCAPE:
          if not self.in_info and not self.in_shop:
            pygame.mixer.music.load(menu_music)
            pygame.mixer.music.play(-1)
            return "ss"
          else:
            self.in_info = False
            self.in_shop = False
        elif event.key == K_e:
          if not self.in_shop and not self.in_info and not self.in_tutorial:
            self.in_shop = True
            self.camera_x_change, self.camera_y_change = 0, 0
            self.shop_notifications_on = False
            pygame.mouse.set_visible(True)
            game_sound_channel.play(door_open)
            #pygame.mixer.Sound.play(door_open)
          elif self.in_info:
            pass
          else:
            self.in_shop = False
            pygame.mouse.set_visible(False)
            game_sound_channel.play(door_close)
            #pygame.mixer.Sound.play(door_close)
        elif event.key == K_r:
          if not self.in_info and not self.in_shop and not self.in_tutorial:
            self.in_info = True
            self.camera_x_change, self.camera_y_change = 0, 0
            pygame.mouse.set_visible(True)
            game_sound_channel.play(info_open_sound)
            #pygame.mixer.Sound.play(info_open_sound)
          elif self.in_shop:
            pass
          else:
            self.in_info = False
            pygame.mouse.set_visible(False)
            game_sound_channel.play(info_close_sound)
            #pygame.mixer.Sound.play(info_close_sound)
        if not self.in_shop and not self.in_info:
          if event.key == K_1:
            if len(self.bullet_hotbar) > 0:
              self.bullet_index = 0
          elif event.key == K_2:
            if len(self.bullet_hotbar) > 1:
              self.bullet_index = 1
          elif event.key == K_3:
            if len(self.bullet_hotbar) > 2:
              self.bullet_index = 2
          elif event.key == K_4:
            if len(self.bullet_hotbar) > 3:
              self.bullet_index = 3
          elif event.key == K_5:
            if len(self.bullet_hotbar) > 4:
              self.bullet_index = 4
          elif event.key == K_6:
            if len(self.bullet_hotbar) > 5:
              self.bullet_index = 5
          elif event.key == K_7:
            if len(self.bullet_hotbar) > 6:
              self.bullet_index = 6
          elif event.key == K_8:
            if len(self.bullet_hotbar) > 7:
              self.bullet_index = 7
          elif event.key == K_9:
            if len(self.bullet_hotbar) > 8:
              self.bullet_index = 8
          elif event.key == K_0:
            if len(self.bullet_hotbar) > 9:
              self.bullet_index = 9
          elif (event.key == K_LSHIFT or event.key == K_RSHIFT):
            self.on_shift = True
            self.shift_pressed = True

          #Summon Extra Enemies
          if self.creative:
            if event.key == K_g:
              if self.on_shift:
                self.summon_enemies.append("green_boss")
              else:
                self.summon_enemies.append("green")
            if event.key == K_o:
              if self.on_shift:
                self.summon_enemies.append("red_boss")
              else:
                self.summon_enemies.append("red")
            if event.key == K_b:
              if self.on_shift:
                self.summon_enemies.append("blue_boss")
              else:
                self.summon_enemies.append("blue")
            if event.key == K_y:
              if self.on_shift:
                self.summon_enemies.append("yellow_boss")
              else:
                self.summon_enemies.append("yellow")
            if event.key == K_t:
              if self.on_shift:
                self.summon_enemies.append("rainbow_boss")
              else:
                self.summon_enemies.append("rainbow")

      if event.type == KEYUP:
        if event.key == K_w:
          self.w_down = False
        elif event.key == K_s:
          self.s_down = False
        elif event.key == K_a:
          self.a_down = False
        elif event.key == K_d:
          self.d_down = False
        elif event.key == K_LSHIFT or event.key == K_RSHIFT:
          self.on_shift = False
    
    """PROCESSING"""
    #Vars
    self.hitboxes = settings["hitboxes"]
    self.camera_shake = settings["camera_shake"]
    self.settings_indicator_arrow_on = settings["ne"]

    #Money
    self.money_txt = MONEY_FONT.render(f'$ {self.money}', True, MONEY_TEXT_COLOR)
    self.money_txt_rect = self.money_txt.get_rect()
    self.money_txt_rect.topright = (WINDOW_WIDTH-MONEY_TEXT_OFFSET, MONEY_TEXT_OFFSET)

    #Settings Button
    self.settings_button.update(self.SETTINGS_BUTTON_HCOLOR, self.SETTINGS_BUTTON_PCOLOR, self.mousePos, self.mouseIsDown)
    if self.settings_button.check_press(self.mousePos, self.mouseUp) and not self.in_tutorial:
      return "sets"

    #Tutorial
    if self.difficulty == "tutorial":
      self.tutorial_frames += 1
      self.tutorial_rect = pygame.Rect(tutorial_texts[self.tutorial_index].boundary_rect.x-TUTORIAL_RECT_OFFSET-tutorial_icon_circle_radius, tutorial_texts[self.tutorial_index].boundary_rect.y-TUTORIAL_RECT_OFFSET, tutorial_texts[self.tutorial_index].boundary_rect.width+TUTORIAL_RECT_OFFSET*2+tutorial_icon_circle_radius, tutorial_texts[self.tutorial_index].boundary_rect.height+TUTORIAL_RECT_OFFSET*2)
      if self.tutorial_frames >= self.tutorial_pause_length and self.in_tutorial:
        self.tutorial_next_text_shown = True
      else:
        self.tutorial_next_text_shown = False
      if self.tutorial_index == 0: #Tutorial message 0
        self.in_tutorial = True
        self.spawn_enemies = False
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.tutorial_index += 1
          self.tutorial_frames = 0
      elif self.tutorial_index == 1: #Tutorial message 1
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.in_tutorial = False
        if not self.in_tutorial:
          if self.w_down:
            self.tutorial_wasd_pressed[0] = True
          if self.s_down:
            self.tutorial_wasd_pressed[1] = True
          if self.a_down:
            self.tutorial_wasd_pressed[2] = True
          if self.d_down:
            self.tutorial_wasd_pressed[3] = True
          if self.tutorial_wasd_pressed[0] and self.tutorial_wasd_pressed[1] and self.tutorial_wasd_pressed[2] and self.tutorial_wasd_pressed[3]:
            self.in_tutorial = True
            self.tutorial_index += 1
            self.tutorial_frames = 0
      
      elif self.tutorial_index == 2: #Tutorial message 2
        if not self.in_tutorial:
          if self.mouseUp:
            self.in_tutorial = True
            self.tutorial_index += 1
            self.tutorial_frames = 0
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.in_tutorial = False
        
      elif self.tutorial_index == 3: #Tutorial message 3
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.tutorial_index += 1
          self.tutorial_frames = 0
      elif self.tutorial_index == 4: #Tutorial message 4
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.in_tutorial = False
        if not self.in_tutorial:
          self.spawn_enemies = True
          if self.green_killed == 1:
            self.in_tutorial = True
            self.tutorial_index += 1
            self.tutorial_frames = 0
            self.spawn_enemies = False
      
      elif self.tutorial_index == 5: #Tutorial message 5
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.in_tutorial = False
        if not self.in_tutorial:
          if self.damage >= 15:
            self.tutorial_index += 1
            self.in_tutorial = True
            self.tutorial_frames = 0
      elif self.tutorial_index == 6: #Tutorial message 6
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length: 
          self.in_tutorial = False
        if not self.in_tutorial:
          self.spawn_enemies = True
          if self.round == 3:
            self.in_tutorial = True
            self.tutorial_index += 1
            self.tutorial_frames = 0
            self.spawn_enemies = False
      
      elif self.tutorial_index == 7: #Tutorial message 7 
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.tutorial_index += 1
          self.tutorial_frames = 0
      elif self.tutorial_index == 8: #Tutorial message 8
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.in_tutorial = False
        if not self.in_tutorial:
          self.spawn_enemies = True
          if self.green_killed >= self.GREEN_NEEDED:
            self.in_tutorial = True
            self.tutorial_index += 1
            self.tutorial_frames = 0
      
      elif self.tutorial_index == 9: #Tutorial message 9
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.tutorial_index += 1
          self.tutorial_frames = 0
      elif self.tutorial_index == 10: #Tutorial message 10
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.tutorial_index += 1
          self.tutorial_frames = 0
      elif self.tutorial_index == 11: #Tutorial message 11
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.in_tutorial = False
        if not self.in_tutorial:
          if self.red_killed >= self.RED_NEEDED:
            self.in_tutorial = True
            self.tutorial_index += 1
            self.tutorial_frames = 0
      
      elif self.tutorial_index == 12: #Tutorial message 12
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.tutorial_index += 1
          self.tutorial_frames = 0
      elif self.tutorial_index == 13: #Tutorial message 13
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.tutorial_index += 1
          self.tutorial_frames = 0
      elif self.tutorial_index == 14: #Tutorial message 14
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          self.in_tutorial = False
        if not self.in_tutorial:
          if self.blue_killed >= self.BLUE_NEEDED:
            self.tutorial_index += 1
            self.in_tutorial = True
            self.tutorial_frames = 0
      
      elif self.tutorial_index == 15:
        if self.mouseUp and self.tutorial_frames >= self.tutorial_pause_length:
          return "completed"
        
    print(self.tutorial_frames)

    if not self.in_shop and not self.in_info:
      #Calculating Camera Offset and Player Movement Calculations
      if self.camera_shake and not self.in_tutorial:
        self.camera_x_change, self.camera_y_change = round((self.mousePos[0]-self.player_x)*CAMERA_MOVEMENT_VALUE), round((self.mousePos[1]-self.player_y)*CAMERA_MOVEMENT_VALUE)
        self.background_x -= self.camera_x_change
        self.background_y -= self.camera_y_change
      else:
        self.camera_x_change = 0
        self.camera_y_change = 0
      self.player_x = MIDDLE_X - self.camera_x_change
      self.player_y = MIDDLE_Y - self.camera_y_change


      #Coords
      self.x_coord_txt = COORD_FONT.render(f'X: {round(self.background_x)*-1+MIDDLE_X-PLAYER_WIDTH//2-self.camera_x_change}', True,  COORD_COLOR)
      self.y_coord_txt = COORD_FONT.render(f'Y: {round(self.background_y)*-1+MIDDLE_Y-PLAYER_HEIGHT//2-self.camera_y_change}', True, COORD_COLOR)
      

      #Shop Button
      self.shop_button.update(SHOP_BUTTON_HOVER_COLOR, SHOP_BUTTON_CLICK_COLOR, self.mousePos, self.mouseIsDown)
      if self.shop_button.check_press(self.mousePos, self.mouseUp) and not self.in_info and not self.in_tutorial:
        self.in_shop = True
        self.camera_x_change, self.camera_y_change = 0, 0
        self.shop_notifications_on = False
        pygame.mouse.set_visible(True)
        game_sound_channel.play(door_open)
        #pygame.mixer.Sound.play(door_open)

      #Info Button
      self.info_button.update(INFO_BUTTON_HOVER_COLOR, INFO_BUTTON_CLICK_COLOR, self.mousePos, self.mouseIsDown)
      self.info_entry = self.bullet_hotbar[self.bullet_index]
      if self.info_button.check_press(self.mousePos, self.mouseUp) and not self.in_shop and not self.in_tutorial:
        self.in_info = True
        self.camera_x_change, self.camera_y_change = 0, 0
        game_sound_channel.play(info_open_sound)
        #pygame.mixer.Sound.play(info_open_sound)
        pygame.mouse.set_visible(True)
      
      #Cursor
      self.cursor_x = self.mousePos[0]
      self.cursor_y = self.mousePos[1]

      #Bullet Cooldowns
      for index, bullet_reload in enumerate(self.bullet_reloads):
        if bullet_reload <= 0:
          self.bullet_available[index] = True
        else:
          self.bullet_reloads[index] -= 1

      #Reloads
      if self.bullet_reloads[self.bullet_index] <= 0:
        self.reload = False
      else:
        self.reload = True


      #Cooldown Rect
      if self.reload:
        cooldown_rect_x = self.cursor_x+self.cursor.get_width()//2-COOLDOWN_RECT_DIMENSIONS[0]//2-8
        cooldown_rect_y = self.cursor_y+self.cursor.get_height()+COOLDOWN_RECT_YOFFSET-8
        self.cooldown_rect.topleft, self.cooldown_rect_bg.topleft = (cooldown_rect_x, cooldown_rect_y), (cooldown_rect_x, cooldown_rect_y)
        self.cooldown_rect.width = COOLDOWN_RECT_DIMENSIONS[0]/self.bullet_cooldowns[self.bullet_index]*(self.bullet_cooldowns[self.bullet_index]-self.bullet_reloads[self.bullet_index])
        if self.cooldown >= self.cooldown_timer:
          self.reload = False
          self.cooldown = 0
          self.cooldown_rect.width = 0

      #Bullets
      if self.mouseIsDown and self.bullet_index != 5 and not self.in_tutorial:
        not_hovering_over_shop = self.mousePos[0]<self.shop_button.x or self.mousePos[0]>self.shop_button.x+self.shop_button.width or self.mousePos[1]<self.shop_button.y or self.mousePos[1]>self.shop_button.y+self.shop_button.height
        not_hovering_over_info = self.mousePos[0]<self.info_button.x or self.mousePos[0]>self.info_button.x+self.info_button.width or self.mousePos[1]<self.info_button.y or self.mousePos[1]>self.info_button.y+self.info_button.height
        not_hovering_over_settings = self.mousePos[0]<self.settings_button.x or self.mousePos[0]>self.settings_button.x+self.settings_button.width or self.mousePos[1]<self.settings_button.y or self.mousePos[1]>self.settings_button.y+self.settings_button.height
        if self.bullet_available[self.bullet_index] and not_hovering_over_shop and not_hovering_over_info and not_hovering_over_settings:
          bullet = Bullet(self.mousePos, WINDOW_WIDTH, WINDOW_HEIGHT, BULLET_SPEED, self.bullet_hotbar[self.bullet_index], self.pierce, self.player_x, self.player_y)
          if self.mana >= bullet.mana_cost:
            self.mana -= bullet.mana_cost
            self.bullets.append(bullet)
            self.bullet_available[self.bullet_index] = False
            self.bullet_reloads[self.bullet_index] = self.bullet_cooldowns[self.bullet_index]
            spell_cast_channel.play(bang_sound)
          else:
            self.not_enough_mana = True
            game_sound_channel.play(error_sound)
            #pygame.mixer.Sound.play(error_sound)
            pass
      #Purple Spells
      elif self.mouseDown and not self.in_tutorial:
        not_hovering_over_shop = self.mousePos[0]<self.shop_button.x or self.mousePos[0]>self.shop_button.x+self.shop_button.width or self.mousePos[1]<self.shop_button.y or self.mousePos[1]>self.shop_button.y+self.shop_button.height
        not_hovering_over_info = self.mousePos[0]<self.info_button.x or self.mousePos[0]>self.info_button.x+self.info_button.width or self.mousePos[1]<self.info_button.y or self.mousePos[1]>self.info_button.y+self.info_button.height
        not_hovering_over_settings = self.mousePos[0]<self.settings_button.x or self.mousePos[0]>self.settings_button.x+self.settings_button.width or self.mousePos[1]<self.settings_button.y or self.mousePos[1]>self.settings_button.y+self.settings_button.height
        if self.bullet_available[self.bullet_index] and not_hovering_over_shop and not_hovering_over_info and not_hovering_over_settings:
          bullet = Bullet(self.mousePos, WINDOW_WIDTH, WINDOW_HEIGHT, BULLET_SPEED, self.bullet_hotbar[self.bullet_index], self.pierce, self.player_x, self.player_y)
          if self.mana >= bullet.mana_cost:
            self.charging_purple = True
            self.bullets.append(bullet)
            purple_charging_channel.play(purple_charging)
            self.bullet_available[self.bullet_index] = False
          else:
            self.not_enough_mana = True
            game_sound_channel.play(error_sound)
            #pygame.mixer.Sound.play(error_sound)
            pass
      #Releases Purple Spell
      if self.charging_purple and self.mouseUp:
        self.bullet_reloads[self.bullet_index] = self.bullet_cooldowns[self.bullet_index]
        self.charging_purple = False
        self.bullet_available[self.bullet_index] = False
        self.mana -= 100 #MODIFY RAINBOW BULLET HERE !!!!!
        purple_charging_channel.stop()
      

      
        

      #PLAYER DASH
      if self.dash != 0 and self.dash_cooldown_frames <= 0 and self.shift_pressed and (self.w_down or self.s_down or self.a_down or self.d_down) and self.mana >= self.dash*2.5:
        self.dashing_frames = 5
        self.mana -= self.dash*2.5
      elif not self.mana >= self.dash*2.5:
        self.not_enough_mana = True
        game_sound_channel.play(error_sound)
        #pygame.mixer.Sound.play(error_sound)
      if self.dashing_frames > 0:
        self.dashing = True
        self.player.fill((200, 200, 200, 50), special_flags=pygame.BLEND_ADD)
        self.dashing_frames -= 1
        if not self.dashing_frames > 0:
          self.dash_cooldown_frames = self.dash_cooldown_time
      else:
        self.dashing = False
        self.player = pygame.image.load(f'resources/images/player_frame{self.player_frame}.png').convert_alpha()
        self.player = pygame.transform.scale(self.player, (PLAYER_WIDTH, PLAYER_HEIGHT))
        if self.player_frame_reversed:
          self.player = pygame.transform.flip(self.player, True, False)
        self.dashing_frames = 0
      
      if self.dashing == False and self.dash_cooldown_frames > 0:
        self.dash_cooldown_frames -= 1
        
            

      #Player Movement
      if (self.w_down or self.d_down or self.s_down or self.a_down) and not self.in_tutorial:

        #Acceleration
        if self.speed_accel < 1 and self.speed_accel != 0:
          self.speed_accel += self.speed_accel_interval
        elif self.speed_accel >= 1:
          self.speed_accel = 1
        else:
          pass

        #Player Frame
        if self.w_down or self.a_down or self.s_down or self.d_down:
          self.player_frames += 1
        if self.player_frames == PLAYER_FRAME_DELAY:
          self.player_frames = 0
          self.player_frame += 1
          if self.player_frame > 8:
            self.player_frame = 0
          self.player = pygame.image.load(f'resources/images/player_frame{self.player_frame}.png').convert_alpha()
          self.player = pygame.transform.scale(self.player, (PLAYER_WIDTH, PLAYER_HEIGHT))
          if self.player_frame_reversed:
            self.player = pygame.transform.flip(self.player, True, False)

        #Dashing and Diagonal Movement
        if (self.w_down and self.d_down) or (self.w_down and self.a_down) or (self.s_down and self.a_down) or (self.s_down and self.d_down):
          self.speed = round(self.speed_value/math.sqrt(2)) * self.speed_accel
        else:
          self.speed = self.speed_value * self.speed_accel
        if self.dashing:
          self.speed += self.dash
      
        #Directions

        #Up/North (W)
        if self.w_down:
          self.background_y += self.speed
          if self.background_y < self.player_y-PLAYER_HEIGHT//2:
            for enemy in self.enemies:
              enemy.y += self.speed
            for bullet in self.bullets:
              bullet.ry += self.speed
          else:
            self.background_y = self.player_y-PLAYER_HEIGHT//2
        
        #Down/South (S)
        if self.s_down:
          self.background_y -= self.speed
          if self.background_y > self.player_y+PLAYER_HEIGHT//2-BACKGROUND_HEIGHT:
            for enemy in self.enemies:
              enemy.y -= self.speed
            for bullet in self.bullets:
              bullet.ry -= self.speed
          else:
            self.background_y = self.player_y+PLAYER_HEIGHT//2-BACKGROUND_HEIGHT

        #Left/West (A)
        if self.a_down:
          self.background_x += self.speed
          self.player_frame_reversed = True
          if self.background_x < self.player_x-PLAYER_WIDTH//2:
            for enemy in self.enemies:
              enemy.x += self.speed
            for bullet in self.bullets:
              bullet.rx += self.speed
          else:
            self.background_x = self.player_x-PLAYER_WIDTH//2

        #Right/East (D)
        if self.d_down:
          self.background_x -= self.speed
          self.player_frame_reversed = False
          if self.background_x > self.player_x+PLAYER_WIDTH//2-BACKGROUND_WIDTH:
            for enemy in self.enemies:
              enemy.x -= self.speed
            for bullet in self.bullets:
              bullet.rx -= self.speed
          else:
            self.background_x = self.player_x+PLAYER_WIDTH//2-BACKGROUND_WIDTH
        
      





      #ENEMIES
      #spawning enemies

      if self.next_round and self.spawn_enemies:
        self.round += 1

        #End Game
        if self.round > len(self.rounds) and not self.difficulty == "tutorial":
          return "completed"
        
        for enemy_type in self.rounds[self.round-1].keys():
          for number in range(self.rounds[self.round-1][enemy_type]):
            while True:
              x = random.randint(0 + round(self.background_x), BACKGROUND_WIDTH + round(self.background_x))
              if x <= self.player_x - 32 - SPAWN_RADIUS or x >= self.player_x - 32 + SPAWN_RADIUS:
                break
            while True:
              y = random.randint(0 + round(self.background_y), BACKGROUND_HEIGHT + round(self.background_y))
              if y <= self.player_y - 32 - SPAWN_RADIUS or y >= self.player_y - 32 + SPAWN_RADIUS:
                break
            self.enemies.append(Enemy(x, y, enemy_type))
        self.next_round = False

      #summons extra enemies
      if self.creative:
        for enemy_type in self.summon_enemies:
          while True:
            x = random.randint(0 + round(self.background_x), BACKGROUND_WIDTH + round(self.background_x))
            if x <= self.player_x - 32 - SPAWN_RADIUS or x >= self.player_x - 32 + SPAWN_RADIUS:
              break
          while True:
            y = random.randint(0 + round(self.background_y), BACKGROUND_HEIGHT + round(self.background_y))
            if y <= self.player_y - 32 - SPAWN_RADIUS or y >= self.player_y - 32 + SPAWN_RADIUS:
              break
          self.enemies.append(Enemy(x, y, enemy_type))
        self.summon_enemies = []

      #Hit enemies
      for bullet in self.bullets:
        for enemy in self.enemies:
          if enemy not in bullet.hit_enemies:
            if bullet.x-bullet.radius > enemy.x-enemy.HITBOX_OFFSET and bullet.pierces > 0 and bullet.y-bullet.radius > enemy.y-enemy.HITBOX_OFFSET and bullet.x+bullet.radius < enemy.x+enemy.width+enemy.HITBOX_OFFSET and bullet.y+bullet.radius < enemy.y+enemy.height+enemy.HITBOX_OFFSET:
              enemy.health-=self.damage*bullet.damage_mult
              enemy.x += int(bullet.x_interval * bullet.knockback)
              enemy.y += int(bullet.y_interval * bullet.knockback)
              enemy.invincible = True
              bullet.hit_enemies.append(enemy)
              bullet.pierces -= 1
              if enemy.health <= 0:
                x_dist = abs(enemy.x - self.player_x)
                y_dist = abs(enemy.y - self.player_y)
                if x_dist < y_dist:
                  if bullet.y < enemy.y:
                    enemy.death_direction = "top"
                  elif bullet.y > enemy.y:
                    enemy.death_direction = "bottom"
                else:
                  if bullet.x < enemy.x:
                    enemy.death_direction = "left"
                  elif bullet.x > enemy.x:
                    enemy.death_direction = "right"
              if bullet.type == "black":
                enemy_hit_channel.play(black_sound)
                #pygame.mixer.Sound.play(black_sound)
              elif bullet.type == "green":
                enemy_hit_channel.play(green_sound)
                #pygame.mixer.Sound.play(green_sound)
                enemy.poison = True
                enemy.poison_frames = 0
              elif bullet.type == 'red':
                enemy_hit_channel.play(red_sound)
                #pygame.mixer.Sound.play(red_sound)
                self.draw_red_explosion.append((bullet.x, bullet.y))
                self.red_explosion_frames.append(0)
                for dif_enemy in self.enemies:
                  distance = math.dist((enemy.x, enemy.y), (dif_enemy.x, dif_enemy.y))
                  if dif_enemy != enemy and distance <= RED_EXPLOSION_RADIUS:
                    dif_enemy.health -= self.damage-(self.damage/RED_EXPLOSION_RADIUS*round(distance))
                    dif_enemy.invincible = True
              elif bullet.type == "blue":
                enemy_hit_channel.play(blue_sound)
                #pygame.mixer.Sound.play(blue_sound)
                enemy.freeze = True
                enemy.freeze_frames = 0
              elif bullet.type == "yellow":
                enemy_hit_channel.play(yellow_sound)
                #pygame.mixer.Sound.play(yellow_sound)
              elif bullet.type == "rainbow":
                enemy_hit_channel.play(rainbow_sound)
                #pygame.mixer.Sound.play(rainbow_sound)

      #deleting enemies
      deleted_enemies = []
      for index, enemy in enumerate(self.enemies):
        damage = 0
        if not self.in_tutorial:
          damage = enemy.update(self.player_x, self.player_y, PLAYER_WIDTH, PLAYER_HEIGHT, self.damage)
        if damage > 0:
          self.health -= damage
          enemy_damage_channel.play(damage_sound)
          #pygame.mixer.Sound.play(damage_sound)
        if enemy.health <= 0:
          enemy.dying = True
        if enemy.dead:
          if enemy.type == "green":
            self.green_killed += 1
          elif enemy.type == "red":
            self.red_killed += 1
          elif enemy.type == "blue":
            self.blue_killed += 1
          elif enemy.type == "yellow":
            self.yellow_killed += 1
          elif enemy.type == "rainbow":
            self.rainbow_killed += 1
          deleted_enemies.insert(0, index)
          self.money += int(enemy.money*self.money_multiplyer*self.difficulty_money_multiplyer)
          coin_sound_channel.play(coin_sound)
          #pygame.mixer.Sound.play(coin_sound)
      for enemy_index in deleted_enemies:
        del self.enemies[enemy_index]

      #Cursor and Camera Moving
      if not self.in_info and not self.in_shop:
        for enemy in self.enemies:
          enemy.x -= self.camera_x_change
          enemy.y -= self.camera_y_change
          enemy.healthbar.x -= self.camera_x_change
          enemy.healthbar.y -= self.camera_y_change
          enemy.g_healthbar.x -= self.camera_x_change
          enemy.g_healthbar.y -= self.camera_y_change


      #Next round
      if len(self.enemies) == 0:
        self.next_round = True
        self.health += int(self.max_health*0.5)
        if self.health > self.max_health:
          self.health = self.max_health
        if self.switch_map == False:
          roundpassed_sound_channel.play(roundpassed_sound)
          #pygame.mixer.Sound.play(roundpassed_sound)
        else:
          self.switch_map = False

      #Round Text
      self.round_text = ROUNDS_TEXT_FONT.render(f'Round: {self.round}/{len(self.rounds)}', True, (0, 0, 0), (255, 255, 255))
      self.round_text_rect = self.round_text.get_rect()
      self.round_text_rect.center = ROUND_TEXT_COORDS


      #Healthbar
      self.healthbar_rect.width = HEALTHBAR_WIDTH / self.max_health * self.health
      self.healthbar_text = HEALTHBAR_FONT.render(f"{self.health}/{self.max_health}", True, (0, 0, 0))
      self.healthbar_text_rect = self.healthbar_text.get_rect()
      self.healthbar_text_rect.center = (HEALTHBAR_X+HEALTHBAR_WIDTH//2, HEALTHBAR_Y+HEALTHBAR_HEIGHT//2+ 3)
      if self.health <= 0:
        return "es"
      
      #Mana Bar
      self.mana += self.max_mana*self.mana_regen_rate
      if self.mana > self.max_mana:
        self.mana = self.max_mana
      self.mana_bar.width = int(MANA_BAR_DIMENSIONS[0]/self.max_mana*self.mana)

      #Hitboxes
      if self.hitboxes:
        self.hitbox = pygame.Rect(self.player_x-PLAYER_WIDTH//2, self.player_y-PLAYER_HEIGHT//2, PLAYER_WIDTH, PLAYER_HEIGHT)

      #Next map
      if self.green_killed >= self.GREEN_NEEDED and self.map == "resources/images/map_white.png":
        self.map = "resources/images/map_green.png"
        if not self.creative:
          self.bullet_hotbar.append("green")
          self.bullet_cooldowns.append(self.cooldown_timer*1.5)
          self.bullet_reloads.append(0)
          self.bullet_available.append(True)
          self.shop_notifications_on = True
          self.info_notifications_on = True
        self.background = pygame.image.load(self.map)
        self.background = pygame.transform.scale(self.background, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.green_buttons = True
        levelup_sound_channel.play(levelup_sound)
        #pygame.mixer.Sound.play(levelup_sound)
        self.switch_map = True
        self.prog_color = (194, 0, 0)
      if self.red_killed >= self.RED_NEEDED and self.map == "resources/images/map_green.png":
        self.map = "resources/images/map_red.png"
        if not self.creative:
          self.bullet_hotbar.append("red")
          self.bullet_cooldowns.append(self.cooldown_timer*5)
          self.bullet_reloads.append(0)
          self.bullet_available.append(True)
          self.shop_notifications_on = True
          self.info_notifications_on = True
        self.background = pygame.image.load(self.map)
        self.background = pygame.transform.scale(self.background, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.red_buttons = True
        levelup_sound_channel.play(levelup_sound)
        #pygame.mixer.Sound.play(levelup_sound)
        self.switch_map = True
        self.prog_color = (0, 91, 207)
      if self.blue_killed >= self.BLUE_NEEDED and self.map == "resources/images/map_red.png":
        self.map = "resources/images/map_blue.png"
        if not self.creative:
          self.bullet_hotbar.append("blue")
          self.bullet_cooldowns.append(self.cooldown_timer*2)
          self.bullet_reloads.append(0)
          self.bullet_available.append(True)
          self.shop_notifications_on = True
          self.info_notifications_on = True
        self.background = pygame.image.load(self.map)
        self.background = pygame.transform.scale(self.background, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.blue_buttons = True
        levelup_sound_channel.play(levelup_sound)
        #pygame.mixer.Sound.play(levelup_sound)
        self.switch_map = True
        self.prog_color = (244, 196, 0)
      if self.yellow_killed >= self.YELLOW_NEEDED and self.map == "resources/images/map_blue.png":
        self.map = "resources/images/map_yellow.png"
        if not self.creative:
          self.bullet_hotbar.append("yellow")
          self.bullet_cooldowns.append(self.cooldown_timer*0.25)
          self.bullet_reloads.append(0)
          self.bullet_available.append(True)
          self.shop_notifications_on = True
          self.info_notifications_on = True
        self.background = pygame.image.load(self.map)
        self.background = pygame.transform.scale(self.background, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        self.yellow_buttons = True
        levelup_sound_channel.play(levelup_sound)
        #pygame.mixer.Sound.play(levelup_sound)
        self.switch_map = True
        self.prog_color = (142, 0, 255)
      if self.rainbow_killed >= self.RAINBOW_NEEDED and self.map == "resources/images/map_yellow.png":
        self.map = "resources/images/map_all.png"
        if not self.creative:
          self.bullet_hotbar.append("rainbow")
          self.bullet_cooldowns.append(self.cooldown_timer*20)
          self.bullet_reloads.append(0)
          self.bullet_available.append(True)
        self.background = pygame.image.load(self.map)
        self.background = pygame.transform.scale(self.background, (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
        levelup_sound_channel.play(levelup_sound)
        #pygame.mixer.Sound.play(levelup_sound)
      
      

      #Progress Bar
      if self.map == "resources/images/map_white.png":
        temp = self.GREEN_NEEDED
        temp1 = self.green_killed
      elif self.map == "resources/images/map_green.png":
        temp = self.RED_NEEDED
        temp1 = self.red_killed
      elif self.map == "resources/images/map_red.png":
        temp = self.BLUE_NEEDED
        temp1 = self.blue_killed
      elif self.map == "resources/images/map_blue.png":
        temp = self.YELLOW_NEEDED
        temp1 = self.yellow_killed
      elif self.map == "resources/images/map_yellow.png":
        temp = self.RAINBOW_NEEDED
        temp1 = self.rainbow_killed
      if self.map == "resources/images/map_all.png":
        pass
      else:
        self.colored_progress_bar.height = PROGRESS_BAR_DIMENSIONS[1]/temp*temp1
        self.colored_progress_bar.bottomleft = (PROGRESS_BAR_COORDS[0], PROGRESS_BAR_COORDS[1]+PROGRESS_BAR_DIMENSIONS[1])


      #Notifications
      if self.shop_notifications_on or self.info_notifications_on:
        self.notification_frames += 1
        if self.notification_frames >= NOTIFICATION_DELAY*2:
          self.notification_frames = 0
      else:
        self.notification_frames = 0
      

      #Indicator Arrow
      self.indicator_arrow, self.indicator_angle, self.indicator_arrow_x, self.indicator_arrow_y = updateIndicator(self.player_x, self.player_y, self.enemies)
      if self.indicator_angle == -1:
        self.indicator_arrow_on = False
      else:
        self.indicator_arrow_on = True

      

      

    #SHOP SCREEN
    if self.in_shop:

      
      #Update Buttons
      self.shop_close_btn.update((190, 90, 60), (130, 30, 5), self.mousePos, self.mouseIsDown)
      self.shop_damage_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)
      self.shop_money_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)
      self.shop_grn_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)
      self.shop_dash_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)
      self.shop_atkspd_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)
      self.shop_mana_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)
      self.shop_spd_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)
      self.shop_pierce_btn.update((230, 230, 230), (150, 150, 150), self.mousePos, self.mouseIsDown)

      #Close Button
      if self.shop_close_btn.check_press(self.mousePos, self.mouseUp):
        self.in_shop = False
        pygame.mouse.set_visible(False)
        game_sound_channel.play(door_close)
        #pygame.mixer.Sound.play(door_close)

      if self.mouseUp:

        #Black Button (damage)
        if len(self.damage_stats) > 0:
          if self.shop_damage_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.damage_price[0]:
              self.damage = self.damage_stats[0]
              self.money -= self.damage_price[0]
              del self.damage_stats[0]
              del self.damage_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.damage_price) > 0:
            self.shop_damage_btn.add_text(SHOP_ITEM_FONT, f"${self.damage_price[0]}", (0, 255, 0), 3)
            self.shop_damage_btn_sub = SHOP_SUB_FONT.render(f"{self.damage} -> {self.damage_stats[0]}", True, (0, 0, 0))
            self.shop_damage_btn_sub_rect = self.shop_damage_btn_sub.get_rect()
            self.shop_damage_btn_sub_rect.center = (SHOP_DAMAGE_BTN_POSITION[0]+SHOP_DAMAGE_BTN_DIMENSIONS[0]//2, SHOP_DAMAGE_BTN_POSITION[1]+SHOP_DAMAGE_BTN_DIMENSIONS[1]+25)
        if len(self.damage_stats) == 0:
          self.shop_damage_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_damage_btn_sub = SHOP_SUB_FONT.render(f"{self.damage}", True, (0, 0, 0))
          self.shop_damage_btn_sub_rect = self.shop_damage_btn_sub.get_rect()
          self.shop_damage_btn_sub_rect.center = (SHOP_DAMAGE_BTN_POSITION[0]+SHOP_DAMAGE_BTN_DIMENSIONS[0]//2, SHOP_DAMAGE_BTN_POSITION[1]+SHOP_DAMAGE_BTN_DIMENSIONS[1]+25)
          
        

        #Black Button (money multiplyer)
        if len(self.money_stats) > 0:
          if self.shop_money_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.money_price[0]:
              self.money_multiplyer = self.money_stats[0]
              self.money -= self.money_price[0]
              del self.money_stats[0]
              del self.money_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.money_price) > 0:
            self.shop_money_btn.add_text(SHOP_ITEM_FONT, f"${self.money_price[0]}", (0, 255, 0), 3)
            self.shop_money_btn_sub = SHOP_SUB_FONT.render(f"{self.money_multiplyer} -> {self.money_stats[0]}", True, (0, 0, 0))
            self.shop_money_btn_sub_rect = self.shop_money_btn_sub.get_rect()
            self.shop_money_btn_sub_rect.center = (SHOP_MONEY_BTN_POSITION[0]+SHOP_MONEY_BTN_DIMENSIONS[0]//2, SHOP_MONEY_BTN_POSITION[1]+SHOP_MONEY_BTN_DIMENSIONS[1]+25)
        if len(self.money_stats) == 0:
          self.shop_money_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_money_btn_sub = SHOP_SUB_FONT.render(f"{self.money_multiplyer}", True, (0, 0, 0))
          self.shop_money_btn_sub_rect = self.shop_money_btn_sub.get_rect()
          self.shop_money_btn_sub_rect.center = (SHOP_MONEY_BTN_POSITION[0]+SHOP_MONEY_BTN_DIMENSIONS[0]//2, SHOP_MONEY_BTN_POSITION[1]+SHOP_MONEY_BTN_DIMENSIONS[1]+25)
          

        
        #Green Button (health)
        if len(self.grn_stats) > 0:
          if self.shop_grn_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.grn_price[0]:
              self.health += self.grn_stats[0]-self.max_health
              self.max_health = self.grn_stats[0]
              self.money -= self.grn_price[0]
              del self.grn_stats[0]
              del self.grn_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.grn_price) > 0:
            self.shop_grn_btn.add_text(SHOP_ITEM_FONT, f"${self.grn_price[0]}", (0, 255, 0), 3)
            self.shop_grn_btn_sub = SHOP_SUB_FONT.render(f"{self.max_health} -> {self.grn_stats[0]}", True, (0, 0, 0))
            self.shop_grn_btn_sub_rect = self.shop_grn_btn_sub.get_rect()
            self.shop_grn_btn_sub_rect.center = (SHOP_GRN_BTN_POSITION[0]+SHOP_GRN_BTN_DIMENSIONS[0]//2, SHOP_GRN_BTN_POSITION[1]+SHOP_GRN_BTN_DIMENSIONS[1]+25)
        if len(self.grn_stats) == 0:
          self.shop_grn_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_grn_btn_sub = SHOP_SUB_FONT.render(f"{self.max_health}", True, (0, 0, 0))
          self.shop_grn_btn_sub_rect = self.shop_grn_btn_sub.get_rect()
          self.shop_grn_btn_sub_rect.center = (SHOP_GRN_BTN_POSITION[0]+SHOP_GRN_BTN_DIMENSIONS[0]//2, SHOP_GRN_BTN_POSITION[1]+SHOP_GRN_BTN_DIMENSIONS[1]+25)
          

        #Green Button (dash)
        if len(self.dash_stats) > 0:
          if self.shop_dash_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.dash_price[0]:
              if self.dash == 0:
                self.skill_hotbar.append("dash")
              self.dash = self.dash_stats[0]
              self.money -= self.dash_price[0]
              del self.dash_stats[0]
              del self.dash_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.dash_price) > 0:
            self.shop_dash_btn.add_text(SHOP_ITEM_FONT, f"${self.dash_price[0]}", (0, 255, 0), 3)
            self.shop_dash_btn_sub = SHOP_SUB_FONT.render(f"{self.dash} -> {self.dash_stats[0]}", True, (0, 0, 0))
            self.shop_dash_btn_sub_rect = self.shop_dash_btn_sub.get_rect()
            self.shop_dash_btn_sub_rect.center = (SHOP_DASH_BTN_POSITION[0]+SHOP_DASH_BTN_DIMENSIONS[0]//2, SHOP_DASH_BTN_POSITION[1]+SHOP_DASH_BTN_DIMENSIONS[1]+25)
        if len(self.dash_stats) == 0:
          self.shop_dash_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_dash_btn_sub = SHOP_SUB_FONT.render(f"{self.dash}", True, (0, 0, 0))
          self.shop_dash_btn_sub_rect = self.shop_dash_btn_sub.get_rect()
          self.shop_dash_btn_sub_rect.center = (SHOP_DASH_BTN_POSITION[0]+SHOP_DASH_BTN_DIMENSIONS[0]//2, SHOP_DASH_BTN_POSITION[1]+SHOP_DASH_BTN_DIMENSIONS[1]+25)
          
        

        #Red Button (atk spd)
        if len(self.atkspd_stats) > 0:
          if self.shop_atkspd_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.atkspd_price[0]:
              self.cooldown_timer = self.atkspd_stats[0]
              for i, cooldown in enumerate(self.bullet_cooldowns):
                self.bullet_cooldowns[i] = self.cooldown_timer*self.reload_mults[i]
                self.bullet_reloads[i] = 0
              self.money -= self.atkspd_price[0]
              del self.atkspd_stats[0]
              del self.atkspd_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.atkspd_price) > 0:
            self.shop_atkspd_btn.add_text(SHOP_ITEM_FONT, f"${self.atkspd_price[0]}", (0, 255, 0), 3)
            self.shop_atkspd_btn_sub = SHOP_SUB_FONT.render(f"{self.cooldown_timer} -> {self.atkspd_stats[0]}", True, (0, 0, 0))
            self.shop_atkspd_btn_sub_rect = self.shop_atkspd_btn_sub.get_rect()
            self.shop_atkspd_btn_sub_rect.center = (SHOP_ATKSPD_BTN_POSITION[0]+SHOP_ATKSPD_BTN_DIMENSIONS[0]//2, SHOP_ATKSPD_BTN_POSITION[1]+SHOP_ATKSPD_BTN_DIMENSIONS[1]+25)
        if len(self.atkspd_stats) == 0:
          self.shop_atkspd_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_atkspd_btn_sub = SHOP_SUB_FONT.render(f"{self.cooldown_timer}", True, (0, 0, 0))
          self.shop_atkspd_btn_sub_rect = self.shop_atkspd_btn_sub.get_rect()
          self.shop_atkspd_btn_sub_rect.center = (SHOP_ATKSPD_BTN_POSITION[0]+SHOP_ATKSPD_BTN_DIMENSIONS[0]//2, SHOP_ATKSPD_BTN_POSITION[1]+SHOP_ATKSPD_BTN_DIMENSIONS[1]+25)
          

        #Red Button (mana)
        if len(self.mana_stats) > 0:
          if self.shop_mana_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.mana_price[0]:
              self.mana += self.mana_stats[0]-self.max_mana
              self.max_mana = self.mana_stats[0]
              self.money -= self.mana_price[0]
              del self.mana_stats[0]
              del self.mana_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.mana_price) > 0:
            self.shop_mana_btn.add_text(SHOP_ITEM_FONT, f"${self.mana_price[0]}", (0, 255, 0), 3)
            self.shop_mana_btn_sub = SHOP_SUB_FONT.render(f"{self.max_mana} -> {self.mana_stats[0]}", True, (0, 0, 0))
            self.shop_mana_btn_sub_rect = self.shop_mana_btn_sub.get_rect()
            self.shop_mana_btn_sub_rect.center = (SHOP_MANA_BTN_POSITION[0]+SHOP_MANA_BTN_DIMENSIONS[0]//2, SHOP_MANA_BTN_POSITION[1]+SHOP_MANA_BTN_DIMENSIONS[1]+25)
        if len(self.mana_stats) == 0:
          self.shop_mana_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_mana_btn_sub = SHOP_SUB_FONT.render(f"{self.max_mana}", True, (0, 0, 0))
          self.shop_mana_btn_sub_rect = self.shop_mana_btn_sub.get_rect()
          self.shop_mana_btn_sub_rect.center = (SHOP_MANA_BTN_POSITION[0]+SHOP_MANA_BTN_DIMENSIONS[0]//2, SHOP_MANA_BTN_POSITION[1]+SHOP_MANA_BTN_DIMENSIONS[1]+25)
          
        
        #Blue Button (spd)
        if len(self.spd_stats) > 0:
          if self.shop_spd_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.spd_price[0]:
              self.speed_value = self.spd_stats[0]
              self.money -= self.spd_price[0]
              del self.spd_stats[0]
              del self.spd_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.spd_price) > 0:
            self.shop_spd_btn.add_text(SHOP_ITEM_FONT, f"${self.spd_price[0]}", (0, 255, 0), 3)
            self.shop_spd_btn_sub = SHOP_SUB_FONT.render(f"{self.speed_value} -> {self.spd_stats[0]}", True, (0, 0, 0))
            self.shop_spd_btn_sub_rect = self.shop_spd_btn_sub.get_rect()
            self.shop_spd_btn_sub_rect.center = (SHOP_SPD_BTN_POSITION[0]+SHOP_SPD_BTN_DIMENSIONS[0]//2, SHOP_SPD_BTN_POSITION[1]+SHOP_SPD_BTN_DIMENSIONS[1]+25)
        if len(self.spd_stats) == 0:
          self.shop_spd_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_spd_btn_sub = SHOP_SUB_FONT.render(f"{self.speed_value}", True, (0, 0, 0))
          self.shop_spd_btn_sub_rect = self.shop_spd_btn_sub.get_rect()
          self.shop_spd_btn_sub_rect.center = (SHOP_SPD_BTN_POSITION[0]+SHOP_SPD_BTN_DIMENSIONS[0]//2, SHOP_SPD_BTN_POSITION[1]+SHOP_SPD_BTN_DIMENSIONS[1]+25)
          
        
        #Yellow Button (Pierce)
        if len(self.pierce_stats) > 0:
          if self.shop_pierce_btn.check_press(self.mousePos, self.mouseUp):
            if self.money >= self.pierce_price[0]:
              self.pierce = self.pierce_stats[0]
              self.money -= self.pierce_price[0]
              del self.pierce_stats[0]
              del self.pierce_price[0]
              game_sound_channel.play(kaching_sound)
              #pygame.mixer.Sound.play(kaching_sound)
            else:
              game_sound_channel.play(error_sound)
              #pygame.mixer.Sound.play(error_sound)
          if len(self.pierce_price) > 0:
            self.shop_pierce_btn.add_text(SHOP_ITEM_FONT, f"${self.pierce_price[0]}", (0, 255, 0), 3)
            self.shop_pierce_btn_sub = SHOP_SUB_FONT.render(f"{self.pierce} -> {self.pierce_stats[0]}", True, (0, 0, 0))
            self.shop_pierce_btn_sub_rect = self.shop_pierce_btn_sub.get_rect()
            self.shop_pierce_btn_sub_rect.center = (SHOP_PIERCE_BTN_POSITION[0]+SHOP_PIERCE_BTN_DIMENSIONS[0]//2, SHOP_PIERCE_BTN_POSITION[1]+SHOP_PIERCE_BTN_DIMENSIONS[1]+25)
        if len(self.pierce_stats) == 0:
          self.shop_pierce_btn.add_text(SHOP_ITEM_FONT, "MAX", (0, 0, 0), 3)
          self.shop_pierce_btn_sub = SHOP_SUB_FONT.render(f"{self.pierce}", True, (0, 0, 0))
          self.shop_pierce_btn_sub_rect = self.shop_pierce_btn_sub.get_rect()
          self.shop_pierce_btn_sub_rect.center = (SHOP_PIERCE_BTN_POSITION[0]+SHOP_PIERCE_BTN_DIMENSIONS[0]//2, SHOP_PIERCE_BTN_POSITION[1]+SHOP_PIERCE_BTN_DIMENSIONS[1]+25)
          
    


    #Info Screen
    if self.in_info:
      self.info_close_btn.update((255, 225, 220), (220, 200, 150), self.mousePos, self.mouseIsDown)
      if self.info_close_btn.check_press(self.mousePos, self.mouseUp):
        self.in_info = False
        pygame.mouse.set_visible(False)
        game_sound_channel.play(info_close_sound)
        #pygame.mixer.Sound.play(info_close_sound)

      #Spell Entries
      if self.info_entry == "black":
        self.spell_name = "Damage"
        self.spell_title_color = (0, 0, 0)
      if self.info_entry == "green":
        self.spell_name = "Poison"
        self.spell_title_color = (0, 255, 0)
      if self.info_entry == "red":
        self.spell_name = "Explosion"
        self.spell_title_color = (255, 0, 0)
      if self.info_entry == "blue":
        self.spell_name = "Freeze"
        self.spell_title_color = (100, 100, 255)
      if self.info_entry == "yellow":
        self.spell_name = "Shard"
        self.spell_title_color = (255, 255, 0)
      if self.info_entry == "rainbow":
        self.spell_name = "Beam"
        self.spell_title_color = (255, 0, 255)

      #Info Picture
      self.info_picture = pygame.image.load(f"resources/images/{self.info_entry}_wand.png")
      self.info_picture = pygame.transform.scale(self.info_picture, INFO_PICTURE_DIMENSIONS)

      self.info_title = INFO_TITLE_FONT.render(f"{self.spell_name} Spell", True, self.spell_title_color)
      self.info_title_rect = self.info_title.get_rect()
      self.info_title_rect.center = INFO_TITLE_COORDS

      self.info_left_button.update(INFO_DBUTTON_HOVER_COLOR, INFO_DBUTTON_PRESSED_COLOR, self.mousePos, self.mouseIsDown)
      if self.info_left_button.check_press(self.mousePos, self.mouseUp):
        if self.bullet_hotbar.index(self.info_entry) != 0:
          self.info_entry = self.bullet_hotbar[self.bullet_hotbar.index(self.info_entry)-1]
          game_sound_channel.play(page_flip)
          #pygame.mixer.Sound.play(page_flip)
      
      self.info_right_button.update(INFO_DBUTTON_HOVER_COLOR, INFO_DBUTTON_PRESSED_COLOR, self.mousePos, self.mouseIsDown)
      if self.info_right_button.check_press(self.mousePos, self.mouseUp):
        if self.bullet_hotbar.index(self.info_entry) != len(self.bullet_hotbar)-1:
          self.info_entry = self.bullet_hotbar[self.bullet_hotbar.index(self.info_entry)+1]
          game_sound_channel.play(page_flip)
          #pygame.mixer.Sound.play(page_flip)

      #Text in Info Screen
      self.info_text_entry = pygame.image.load(f"resources/images/{self.info_entry}_spell_entry.png")
      self.info_text_entry = pygame.transform.scale(self.info_text_entry, (INFO_TEXT_ENTRY_DIMENSIONS))
      self.info_text_entry_rect = self.info_text_entry.get_rect()
      self.info_text_entry_rect.topleft = INFO_TEXT_ENTRY_COORDS

      if self.bullet_hotbar.index(self.info_entry) == len(self.bullet_hotbar)-1:
        self.info_notifications_on = False

      






    """DRAW TO SCREEN"""
    WINDOW.fill(self.color_bg)

    #Background
    #pygame.draw.rect(WINDOW, (255, 255, 255), self.background)
    WINDOW.blit(self.background, (self.background_x, self.background_y))
    self.background_x += self.camera_x_change
    self.background_y += self.camera_y_change

    #Nearest Enemy Indicator
    if self.indicator_arrow_on and self.settings_indicator_arrow_on:
      WINDOW.blit(self.indicator_arrow, (self.indicator_arrow_x, self.indicator_arrow_y))

    #Bullets
    if not self.in_info and not self.in_shop:
      delete_bullets = []
      for index, bullet in enumerate(self.bullets):
        bullet.update(self.mouseUp, self.mousePos, BULLET_SPEED)
        if bullet.x < 0-bullet.radius*5 or bullet.x > WINDOW_WIDTH+bullet.radius*5 or bullet.y < 0-bullet.radius*5 or bullet.y > WINDOW_HEIGHT+bullet.radius*5 or bullet.pierces <= 0:
          delete_bullets.insert(0, index)
        bullet.x -= self.camera_x_change
        bullet.y -= self.camera_y_change
        pygame.draw.circle(WINDOW, bullet.color, (bullet.x, bullet.y), bullet.radius)
      for bullet_index in delete_bullets:
        del self.bullets[bullet_index]

      #Red Explosion
      delete = []
      for i, coords in enumerate(self.draw_red_explosion):
        if self.red_explosion_frames[i] == 0:
          pygame.draw.circle(WINDOW, (255, 0, 0), coords, RED_EXPLOSION_RADIUS*0.25)
        elif self.red_explosion_frames[i] == 1:
          pygame.draw.circle(WINDOW, (255, 0, 0), coords, RED_EXPLOSION_RADIUS*0.5)
        elif self.red_explosion_frames[i] == 2:
          pygame.draw.circle(WINDOW, (255, 0, 0), coords, RED_EXPLOSION_RADIUS*0.9)
        elif self.red_explosion_frames[i] == 3:
          pygame.draw.circle(WINDOW, (255, 0, 0), coords, RED_EXPLOSION_RADIUS)
        elif self.red_explosion_frames[i] == 4:
          pygame.draw.circle(WINDOW, (255, 0, 0), coords, RED_EXPLOSION_RADIUS*0.75)
        elif self.red_explosion_frames[i] == 5:
          pygame.draw.circle(WINDOW, (255, 0, 0), coords, RED_EXPLOSION_RADIUS*0.25)
        self.red_explosion_frames[i] += 1
        if self.red_explosion_frames[i] > 5:
          delete.insert(0, i)
        for entry in delete:
          del self.draw_red_explosion[entry]
          del self.red_explosion_frames[entry]
    
    #Player
    WINDOW.blit(self.player, (self.player_x-PLAYER_WIDTH//2, self.player_y-PLAYER_HEIGHT//2))

    #Enemies
    for enemy in self.enemies:
      if enemy.invincible or enemy.poison or enemy.freeze:
        if enemy.invincible:
          enemy.image.fill((255, 0, 0, enemy.invincible_alpha), special_flags=pygame.BLEND_ADD)
        if enemy.poison:
          enemy.image.fill((25, 100, 25, 100), special_flags=pygame.BLEND_ADD)
        if enemy.freeze:
          enemy.image.fill((75, 75, 200, 100), special_flags=pygame.BLEND_ADD)
      WINDOW.blit(enemy.image, (enemy.x, enemy.y))
      if self.hitboxes:
        rect = pygame.Rect(enemy.x, enemy.y, enemy.width, enemy.height)
        pygame.draw.rect(WINDOW, (0, 0, 0), rect, HITBOX_WIDTH)
      if not enemy.dying:
        pygame.draw.rect(WINDOW, (255, 0, 0), enemy.healthbar)
        pygame.draw.rect(WINDOW, (0, 255, 0), enemy.g_healthbar)
      enemy.x += self.camera_x_change
      enemy.y += self.camera_y_change
      


    #Player Hitbox
    if self.hitboxes:
      pygame.draw.rect(WINDOW, (0, 0, 0), self.hitbox, HITBOX_WIDTH)


    #Healthbar
    pygame.draw.rect(WINDOW, (255, 0, 0), self.healthbar_bg_rect)
    pygame.draw.rect(WINDOW, (0, 255, 0), self.healthbar_rect)
    pygame.draw.rect(WINDOW, (0, 0, 0), self.healthbar_bg_rect, 5)
    WINDOW.blit(self.healthbar_text, self.healthbar_text_rect)

    #Coordinates
    if self.creative:
      WINDOW.blit(self.x_coord_txt, (X_COORD_TEXT_X, X_COORD_TEXT_Y))
      WINDOW.blit(self.y_coord_txt, (Y_COORD_TEXT_X, Y_COORD_TEXT_Y))

    #Shop Button_notification
    if self.notification_frames >= NOTIFICATION_DELAY and self.shop_notifications_on:
      pygame.draw.rect(WINDOW, NOTIFICATION_COLOR, self.shop_notification)
    
    #Info Button_notification
    if self.notification_frames >= NOTIFICATION_DELAY and self.info_notifications_on:
      pygame.draw.rect(WINDOW, NOTIFICATION_COLOR, self.info_notification)

    #Shop Button
    self.shop_button.draw(WINDOW)

    #Info Button
    self.info_button.draw(WINDOW)

    #Progress Bar
    if self.map != "resources/images/map_all.png":
      pygame.draw.rect(WINDOW, self.prog_color, self.colored_progress_bar)
      pygame.draw.rect(WINDOW, (0, 0, 0), self.progress_bar, 5)

    #Mana Bar
    pygame.draw.rect(WINDOW, MANA_BAR_BACK_COLOR, self.mana_background_bar)
    pygame.draw.rect(WINDOW, MANA_BAR_COLOR, self.mana_bar)
    pygame.draw.rect(WINDOW, (0, 0, 0), self.mana_background_bar, 5)

    #Mana Notification
    if self.not_enough_mana:
      self.not_enough_mana_frames += 1
      text = MANA_NOTIFICATION_FONT.render("* Not Enough Mana *", True, MANA_NOTIFICATION_COLOR)
      text_rect = text.get_rect()
      text_rect.center = MANA_NOTIFICATION_POSITION
      WINDOW.blit(text, text_rect)
      if self.not_enough_mana_frames >= self.not_enough_mana_time:
        self.not_enough_mana = False
        self.not_enough_mana_frames = 0

    #Rounds Text
    WINDOW.blit(self.round_text, self.round_text_rect)

    #Escape Text
    WINDOW.blit(self.escape_text, self.escape_text_rect)


    #Bullet Hotbar
    overall_hotbar_length = len(self.bullet_hotbar)*HOTBAR_BOX_DIMENSIONS[0]+(len(self.bullet_hotbar)-1)*HOTBAR_BOX_XOFFSET
    for index, bullet_entry in enumerate(self.bullet_hotbar):
      rect = pygame.Rect(MIDDLE_X-overall_hotbar_length//2+index*(HOTBAR_BOX_DIMENSIONS[0]+HOTBAR_BOX_XOFFSET), HOTBAR_BOX_Y, HOTBAR_BOX_DIMENSIONS[0], HOTBAR_BOX_DIMENSIONS[1])
      if index == self.bullet_index:
        rect.y += HOTBAR_BOX_YOFFSET
      text = HOTBAR_BOX_FONT.render(f"{index+1}", True, (0, 0, 0))
      text_rect = text.get_rect()
      text_rect.bottomright = (rect.x+HOTBAR_BOX_DIMENSIONS[0]-5, rect.y+HOTBAR_BOX_DIMENSIONS[1]-5)
      pygame.draw.rect(WINDOW, (255, 255, 255), rect)
      pygame.draw.rect(WINDOW, (0, 0, 0), rect, 5)
      image = pygame.image.load(f"resources/images/{self.bullet_hotbar[index]}_wand.png").convert_alpha()
      image_rect = image.get_rect()
      image_rect.center = (rect.x+rect.width//2, rect.y+rect.height//2)
      WINDOW.blit(image, image_rect)
      WINDOW.blit(text, text_rect)

      if self.bullet_reloads[index] > 0:
        temp = HOTBAR_BOX_DIMENSIONS[1]/self.bullet_cooldowns[index]*self.bullet_reloads[index]
        yoff = 0
        if index == self.bullet_index:
          yoff = HOTBAR_BOX_YOFFSET
        surface = pygame.Surface((HOTBAR_BOX_DIMENSIONS[0], temp))
        surface.set_alpha(200)
        surface.fill((150, 150, 150))
        WINDOW.blit(surface, (MIDDLE_X-overall_hotbar_length//2+index*(HOTBAR_BOX_DIMENSIONS[0]+HOTBAR_BOX_XOFFSET), HOTBAR_BOX_Y+(HOTBAR_BOX_DIMENSIONS[1]-temp)+yoff))

    #Skill Hotbar
    overall_skill_hotbar_length = len(self.skill_hotbar)*SKILL_HOTBAR_BOX_DIMENSIONS[0]+(len(self.bullet_hotbar)-1)*HOTBAR_BOX_XOFFSET
    for index, skill_entry in enumerate(self.skill_hotbar):
      rect = pygame.Rect(WINDOW_WIDTH-overall_skill_hotbar_length+index*(SKILL_HOTBAR_BOX_DIMENSIONS[0]+HOTBAR_BOX_XOFFSET), HOTBAR_BOX_Y, SKILL_HOTBAR_BOX_DIMENSIONS[0], SKILL_HOTBAR_BOX_DIMENSIONS[1])
      if skill_entry == "dash":
        text = SKILL_HOTBAR_BOX_FONT.render("shift", True, (0, 0, 0))
      text_rect = text.get_rect()
      text_rect.bottomright = (rect.x+SKILL_HOTBAR_BOX_DIMENSIONS[0]-5, rect.y+SKILL_HOTBAR_BOX_DIMENSIONS[1]-5)
      pygame.draw.rect(WINDOW, (255, 255, 255), rect)
      pygame.draw.rect(WINDOW, (0, 0, 0), rect, 5)
      image = pygame.image.load(f"resources/images/{skill_entry}_image.png").convert_alpha()
      image_rect = image.get_rect()
      image_rect.center = (rect.x+rect.width//2, rect.y+rect.height//2)
      WINDOW.blit(image, image_rect)
      WINDOW.blit(text, text_rect)
      if skill_entry == "dash" and self.dash_cooldown_frames > 0:
        temp = round(SKILL_HOTBAR_BOX_DIMENSIONS[1]/self.dash_cooldown_time*self.dash_cooldown_frames)
        surface = pygame.Surface((SKILL_HOTBAR_BOX_DIMENSIONS[0], temp))
        surface.set_alpha(200)
        surface.fill((150, 150, 150))
        WINDOW.blit(surface, (WINDOW_WIDTH-overall_skill_hotbar_length+index*(SKILL_HOTBAR_BOX_DIMENSIONS[0]+HOTBAR_BOX_XOFFSET), HOTBAR_BOX_Y+(SKILL_HOTBAR_BOX_DIMENSIONS[1]-temp)))

        


    #Cursor
    WINDOW.blit(self.cursor, (self.cursor_x+CURSOR_X_OFFSET, self.cursor_y+CURSOR_Y_OFFSET))

    #Cooldown Timer
    if self.reload:
      pygame.draw.rect(WINDOW, COOLDOWN_RECT_BACK_COLOR, self.cooldown_rect_bg)
      pygame.draw.rect(WINDOW, COOLDOWN_RECT_FRONT_COLOR, self.cooldown_rect)

    

    #SHOP SCREEN
    if self.in_shop:
      WINDOW.blit(self.shop_bg_rect, (0, 0))
      #pygame.draw.rect(WINDOW, SHOP_BG_COLOR, self.shop_back, border_radius=10)
      #pygame.draw.rect(WINDOW, (0, 0, 0), self.shop_back, 5, 10)
      WINDOW.blit(self.shop_back, (SHOP_BG_OFFSET, SHOP_BG_OFFSET))
      self.shop_close_btn.draw(WINDOW)

      self.shop_damage_btn.draw(WINDOW)
      WINDOW.blit(SHOP_DAMAGE_BTN_TITLE, shop_damage_btn_title_rect)
      WINDOW.blit(self.shop_damage_btn_sub, self.shop_damage_btn_sub_rect)

      self.shop_money_btn.draw(WINDOW)
      WINDOW.blit(SHOP_MONEY_BTN_TITLE, shop_money_btn_title_rect)
      WINDOW.blit(self.shop_money_btn_sub, self.shop_money_btn_sub_rect)

      if self.green_buttons:
        self.shop_grn_btn.draw(WINDOW)
        WINDOW.blit(SHOP_GRN_BTN_TITLE, shop_grn_btn_title_rect)
        WINDOW.blit(self.shop_grn_btn_sub, self.shop_grn_btn_sub_rect)

        self.shop_dash_btn.draw(WINDOW)
        WINDOW.blit(SHOP_DASH_BTN_TITLE, shop_dash_btn_title_rect)
        WINDOW.blit(self.shop_dash_btn_sub, self.shop_dash_btn_sub_rect)
      
      if self.red_buttons:
        self.shop_atkspd_btn.draw(WINDOW)
        WINDOW.blit(SHOP_ATKSPD_BTN_TITLE, shop_atkspd_btn_title_rect)
        WINDOW.blit(self.shop_atkspd_btn_sub, self.shop_atkspd_btn_sub_rect)

        self.shop_mana_btn.draw(WINDOW)
        WINDOW.blit(SHOP_MANA_BTN_TITLE, shop_mana_btn_title_rect)
        WINDOW.blit(self.shop_mana_btn_sub, self.shop_mana_btn_sub_rect)

      if self.blue_buttons:
        self.shop_spd_btn.draw(WINDOW)
        WINDOW.blit(SHOP_SPD_BTN_TITLE, shop_spd_btn_title_rect)
        WINDOW.blit(self.shop_spd_btn_sub, self.shop_spd_btn_sub_rect)

      if self.yellow_buttons:
        self.shop_pierce_btn.draw(WINDOW)
        WINDOW.blit(SHOP_PIERCE_BTN_TITLE, shop_pierce_btn_title_rect)
        WINDOW.blit(self.shop_pierce_btn_sub, self.shop_pierce_btn_sub_rect)
    
    #INFO SCREEN
    if self.in_info:
      WINDOW.blit(self.info_bg_rect, (0, 0))
      WINDOW.blit(self.info_back, (INFO_BG_OFFSET, INFO_BG_OFFSET))
      #pygame.draw.rect(WINDOW, INFO_BG_COLOR, self.info_back, border_radius=10)
      #pygame.draw.rect(WINDOW, (0, 0, 0), self.info_back, 5, 10)
      self.info_close_btn.draw(WINDOW)

      WINDOW.blit(self.info_picture, INFO_PICTURE_COORDS)
      WINDOW.blit(self.info_title, self.info_title_rect)

      if self.bullet_hotbar.index(self.info_entry) != 0:
        self.info_left_button.draw(WINDOW)
      if self.bullet_hotbar.index(self.info_entry) < len(self.bullet_hotbar) - 1:
        self.info_right_button.draw(WINDOW)

      WINDOW.blit(self.info_text_entry, self.info_text_entry_rect)
    
    #Money
    WINDOW.blit(self.money_txt, self.money_txt_rect)

    #Spawning Enemies Text
    if self.creative:
      self.spawning_enemies_text.draw(WINDOW)
    
    #Tutorial
    if self.difficulty == "tutorial" and self.in_tutorial:
      if tutorial_bgs[self.tutorial_index] == None:
        WINDOW.blit(default_tutorial_bg, (0, 0))
      else:
        for surface in tutorial_bgs[self.tutorial_index]:
          WINDOW.blit(surface[0], surface[1])
      pygame.draw.rect(WINDOW, (255, 255, 255), self.tutorial_rect)
      pygame.draw.rect(WINDOW, (0, 0, 0), self.tutorial_rect, 5)
      tutorial_texts[self.tutorial_index].draw(WINDOW)
      WINDOW.blit(tutorial_icon, (self.tutorial_rect.x-tutorial_icon_diameter//2, self.tutorial_rect.y-(tutorial_icon_diameter-self.tutorial_rect.height)//2))
      pygame.draw.circle(WINDOW, (0, 0, 0), (self.tutorial_rect.x, self.tutorial_rect.y+self.tutorial_rect.height//2), tutorial_icon_circle_radius, 5)

      if self.tutorial_next_text_shown:
        WINDOW.blit(tutorial_next_text, tutorial_next_text_rect)

    #Tutorial Tips
    if self.difficulty == "tutorial" and not self.in_tutorial:
      if self.tutorial_index == 1:
        for i, direction in enumerate(self.tutorial_wasd_pressed):
          if i == 0 and direction == 0:
            WINDOW.blit(tutorial_w_txt, tutorial_w_txt_rect)
          elif i == 1 and direction == 0:
            WINDOW.blit(tutorial_s_txt, tutorial_s_txt_rect)
          elif i == 2 and direction == 0:
            WINDOW.blit(tutorial_a_txt, tutorial_a_txt_rect)
          elif i == 3 and direction == 0:
           WINDOW.blit(tutorial_d_txt, tutorial_d_txt_rect)
      
      if tutorial_hints[self.tutorial_index] != None:
        WINDOW.blit(tutorial_objective_text, tutorial_objective_text_rect)
        tutorial_hints[self.tutorial_index].draw(WINDOW)

    self.settings_button.draw(WINDOW)

    return "gs"





 



 
# The main function that controls the game
async def main () :

  pygame.mixer.music.load(menu_music)
  pygame.mixer.music.play(-1)

  """INITIATE THE SCREENS"""
  ss = Start_screen()
  ss.running = True

  ds = Difficulty_Screen()
  ds.running = False

  gs = GameScreen("medium")
  gs.running = False

  es = End_screen()
  es.running = False

  i_s = Instructions_Screen()
  i_s.running = False

  cs = Credits_Screen()
  cs.running = False

  sets = Settings_Screen()
  sets.running = False

  completed_screen = Completed_Screen()
  completed_screen.running = False

  init = True
  previous_screen = ""

  #Vars
  difficulty = "medium"
  global settings
  global settings_previous_screen


  """MAIN GAME LOOP"""
  while True :


    """USER INPUT"""
    events = []
    for event in pygame.event.get() :
      events.append(event)
    

    """ACTIVATE SCREENS"""
    if ss.running:
      state = ss.run(events)
      if state == "sets":
        settings_previous_screen = "ss"
    
    if ds.running:
      state, difficulty = ds.run(events)

    if gs.running:
      state = gs.run(events)
      if state == "sets":
        settings_previous_screen = "gs"
    
    if es.running:
      state = es.run(events)
      if state == "ss":
        pass
        pygame.mixer.music.load(menu_music)
        pygame.mixer.music.play(-1)
    
    if i_s.running:
      state = i_s.run(events)
    

    #Runs Settings Screen
    if sets.running:
      state, settings = sets.run(events, settings_previous_screen)
      #SFX
      if settings["sfx"]:
        for sound in sfx:
          sound.set_volume(settings["volume"]/100)
      else:
        for sound in sfx:
          sound.set_volume(0)
      
      #Music
      if settings["music"]:
        pygame.mixer.music.set_volume(settings["volume"]/100)
      else:
        pygame.mixer.music.set_volume(0)
    

    if cs.running:
      state = cs.run(events)
    
    if completed_screen.running:
      state = completed_screen.run(events)


    #Checks if a new screen is displayed
    if state != previous_screen:
      init = True


    if init:
      #Makes sure the screens are running as they should
      #Start Screen
      if state == "ss":
        pygame.mouse.set_visible(True)
        ss.running = True
        ds.running = False
        gs.running = False
        es.running = False
        i_s.running = False
        sets.running = False
        cs.running = False
        completed_screen.running = False
      #Difficulty Screen
      elif state == "ds":
        ss.running = False
        ds.running = True
        gs.running = False
        es.running = False
        i_s.running = False
        sets.running = False
        cs.running = False
        completed_screen.running = False
      #Game Screen (After visiting the settings screen)
      elif state == "gs" and previous_screen == "sets":
        pygame.mouse.set_visible(False)
        pygame.mixer.music.load(game_music)
        pygame.mixer.music.play(-1)
        ss.running = False
        ds.running = False
        gs.running = True
        es.running = False
        i_s.running = False
        sets.running = False
        cs.running = False
        completed_screen.running = False
      #Game Screen
      #Runs the main game loop
      elif state == "gs":
        gs = GameScreen(difficulty)
        pygame.mouse.set_visible(False)
        pygame.mixer.music.load(game_music)
        pygame.mixer.music.play(-1)
        ss.running = False
        ds.running = False
        gs.running = True
        es.running = False
        i_s.running = False
        sets.running = False
        cs.running = False
        completed_screen.running = False
      #End Screen
      elif state == "es":
        pygame.mouse.set_visible(True)
        pygame.mixer.music.stop()
        game_sound_channel.play(fail_sound)
        pygame.mixer.Sound.play(fail_sound)
        ss.running = False
        ds.running = False
        gs.running = False
        es.running = True
        i_s.running = False
        sets.running = False
        cs.running = False
        completed_screen.running = False
      #Instructions Screen
      elif state == "i_s":
        pygame.mouse.set_visible(True)
        ss.running = False
        ds.running = False
        gs.running = False
        es.running = False
        i_s.running = True
        sets.running = False
        cs.running = False
        completed_screen.running = False
      #Settings Screen
      #Screen to change settings (duh!)
      elif state == "sets":
        pygame.mouse.set_visible(True)
        ss.running = False
        ds.running = False
        gs.running = False
        es.running = False
        i_s.running = False
        sets.running = True
        cs.running = False
        completed_screen.running = False
      #Credits Screen
      elif state == "cs":
        pygame.mouse.set_visible(True)
        ss.running = False
        ds.running = False
        gs.running = False
        es.running = False
        i_s.running = False
        sets.running = False
        cs.running = True
        completed_screen.running = False
      #Completed Screen
      elif state == "completed":
        pygame.mouse.set_visible(True)
        pygame.mixer.music.stop()
        ss.running = False
        ds.running = False
        gs.running = False
        es.running = False
        i_s.running = False
        sets.running = False
        cs.running = False
        completed_screen.running = True
      init = False

    previous_screen = state


 
    """UPDATE and FPS"""
    pygame.display.update()
    fpsClock.tick(FPS)

    await asyncio.sleep(0)


asyncio.run(main())

#Well hello there. I didn't expect to see you here. poggers? I don't really know what else to write here... Are you having a good day? Mine is pretty okay. 
#Had some stuff happen in robotics, but that is unavoidable and hopefully I get better. If you're doing well I hope you have a fantastic rest of your day, and if you aren't
#I hope you know that there are people willing to support you no matter what. Welp there's my rant have a great life.
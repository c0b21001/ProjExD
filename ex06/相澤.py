import pygame as pg
from pygame.locals import *
import csv


#画面サイズの設定
screen_width = 1800
screen_height = 900
#1マスのサイズを設定
tile_size = 50
#画面サイズを１マスのサイズで割った数を取得
ROWS = int(screen_width / tile_size) #24
COLUMNS = int(screen_height / tile_size) #12
#プレイヤーのサイズ
PLAYER_SIZE = 50
 
#画面のサイズ指定
SCREEN = pg.display.set_mode((screen_width, screen_height))
#タイトルの設定
pg.display.set_caption('Platform')	
#時間の設定
CLOCK = pg.time.Clock()
FPS = 60

#画面の左右の端を設定（この範囲を超えるとバックグラウンドが動く（プレイヤーは止まる））
RIGHT_EDGE = screen_width - int(screen_width / 5)
LEFT_EDGE = int(screen_width / 5)
#画面の上下の端を設定（この範囲を超えるとバックグラウンドが動く（プレイヤーは止まる））
UP_EDGE = screen_height - int(screen_height / 5)
DOWN_EDGE =int(screen_height / 5)
#csvからデータを呼び出して、リストに格納する。
stage_data = []

bg_y = 0

#with openでファイルを開き、1行づつ空のリストに格納
with open("team\ProjExD-1/ex06/stage.csv",newline='') as data:
    reader = csv.reader(data,delimiter=',')
    for row in reader:
        #リストに格納する内容は文字列型(str)になっているので数値型(int)に変換します。
        #map関数はリストの内容1つ毎に関数を実行してくれます。関数実行後rowに再代入します。
        row = list(map(int,(row)))
        #ここでprintを記述すればどのような内容がリストに格納されるか確認できます。
        # print(row)
        stage_data.append(row)


class Stage():
	def __init__(self, data):
		#空のリストを用意
		self.tile_list = []
		#4枚のタイルが1つになった画像を呼び出します
		self.sprite_sheet = pg.image.load("team\ProjExD-1/ex06/img/tiles.png").convert_alpha()
		image = pg.image.load("team\ProjExD-1/ex06/img/egg.jpg").convert_alpha()
		
		#引数dataリスト内の位置とサイズ情報を格納していく
		#dataは先ほど作成したstage_data
		row_count = 0
		for row in data:
			col_count = 0
			for tile in row:
				if tile == 0:
					self.img = self.get_image(self.sprite_sheet,0,0,tile_size,tile_size)				
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)
				if tile == 1:
					self.img = self.get_image(self.sprite_sheet,51,0,tile_size,tile_size)
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)
				if tile == 2:
					self.img = self.get_image(self.sprite_sheet,0,51,tile_size,tile_size)
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)
				if tile == 3:
					self.img = self.get_image(self.sprite_sheet,51,51,tile_size,tile_size)				
					self.img_rect = self.tile_info(self.img,col_count,row_count)
					tile = (self.img, self.img_rect)
					self.tile_list.append(tile)	
				col_count += 1
			row_count += 1
	
	#先に呼び出した画像から情報を取得するメソッド		
	def tile_info(self,image,col_count,row_count):
		rect = image.get_rect()
		rect.x = col_count * tile_size
		rect.y = row_count * tile_size
		return rect

	#4つのタイルの画像から1つ取得するメソッド（x、yで取得する画像の開始位置を指定）
	def get_image(self,sheet, x, y, width, height):
			image = pg.Surface((width, height))
			image.blit(sheet, (0, 0), (x, y, width, height))
			return image

	#描画用メソッド（tile[0]に画像,tile[1]に描画位置が格納されている）
	def draw(self):
		for tile in self.tile_list:
			SCREEN.blit(tile[0],tile[1])
	
	#プレイヤーの位置がEDGEと同じ値になったら実行するメソッド。
#タイルのxを足したり、引いたりして描画位置を調節する(下の画像参照）
	def scroll_front(self):	
		for tile in self.tile_list:
			tile[1].x -= 5
	def scroll_back(self):	
		for tile in self.tile_list:
			tile[1].x += 5
	def scroll_head(self):	
		for tile in self.tile_list:
			tile[1].y -= 5
	def scroll_foot(self):	
		for tile in self.tile_list:
			tile[1].y += 5


class Player(pg.sprite.Sprite):
	def __init__(self, x, y):
		super().__init__()
		#画像の設定
		image = pg.image.load("team\ProjExD-1/ex06/img/tori.png").convert_alpha()
		image = pg.transform.scale(image,(PLAYER_SIZE,PLAYER_SIZE))
		self.right_image = image
		#元の画像が左向きなので画像を180度Y軸に反転させる
		self.left_image = pg.transform.flip(image,True,False)
		self.image = self.right_image
		#画像からrectサイズを取得
		self.rect = self.image.get_rect()
		#位置の設定
		self.rect.x = x
		self.rect.y = y
		#画像の高さと幅の取得
		self.width = self.image.get_width()
		self.height = self.image.get_height()
		#y軸方向の速度設定、とりあえず0にしておく
		self.vel_y = 0
		#jumpしているかのフラグ
		self.jumped = False
		#地面についているかのフラグ
		self.on_ground = True 
		#壁についているかのフラグ（澤木）
		self.wall = False
		#空中にいる状態かのフラグ
		self.in_the_air = False
		#死亡したかのフラグ
		self.dead = False
		#向きの設定
		self.direction = 0
		self.RIGHT = False
		self.LEFT  = False
		self.UP = False
		self.Down = True
		#動きの幅（量）設定(始めは0で設定）
		self.dx = 0
		self.dy = 0

	#操作のメソッド
	def key_con(self,data):
		#x軸、y軸の移動幅 初期化
		self.dx = 0
		self.dy = 0							

		#キー操作関数
		key = pg.key.get_pressed()
		#右移動キー
		if key[K_RIGHT]and self.in_the_air == True: #移動キーを押したときと、空中にいる間だけ。
			self.RIGHT,self.LEFT = True, False
			self.direction = 0
			self.dx += 5
		if not key[K_RIGHT]:
			self.RIGHT = False
		
		#左移動キー
		if key[K_LEFT] and self.in_the_air == True:
			self.RIGHT,self.LEFT = False, True
			self.direction = 1
			self.dx -= 5
		if not key[K_LEFT]:
			self.LEFT = False

		#jumpキーを押した時、ジャンプするかフラグで判断。条件に当てはまればジャンプ実行
		if key[K_SPACE] and self.jumped == False and self.on_ground == True and self.in_the_air == False:
			self.UP,self.DONW = True, False
			self.jumped = True
			self.vel_y = -20
			self.on_ground = False
		if not key[K_SPACE]:
			self.UP,self.DOWN = False,False 
		#jumpのキーを放した（false）ら、jumpフラグをfalseに戻す
		if not key[K_SPACE]:
			self.jumped = False

		#重力の追加（後に設定するメソッドで）
		self.add_gravity()

		#X軸当たり判定TRUEならdxを0にする
		if self.collisionX(data):
			self.dx = 0
		self.collisionY(data)

		#プレイヤーが画面端に来た場合の処理
		if self.rect.x > RIGHT_EDGE and self.RIGHT:
			self.dx = 0
		if self.rect.x <= 0 and self.LEFT:
			self.dx = 0
		if self.rect.x >= screen_width:
			self.dx = 0
		if self.rect.y > UP_EDGE and self.UP:
			self.dy = 0
		if self.rect.y <= 0 and self.DOWN:
			self.dy = 0
		if self.rect.y >= screen_height:
			self.dy = 0

		#プレイヤーの位置に移動速度を足す
		self.rect.x += self.dx
		self.rect.y += self.dy

		#プレイヤーが地面のギャップに落ちた時の処理
		if self.rect.top >= screen_height:
			self.dead = True
			self.kill()

	#X軸方向の当たり判定
	def collisionX(self,data):
		for tile in data:
			if tile[1].colliderect(self.rect.x + self.dx, self.rect.y, self.width, self.height):
				self.wall = True #澤木

	#Y軸方向の当たり判定			
	def collisionY(self,data):
		for tile in data:
			if tile[1].colliderect(self.rect.x, self.rect.y + self.dy, self.width, self.height):
				if self.vel_y < 0:
					self.dy = tile[1].bottom - self.rect.top
					self.vel_y = 0
	
				elif self.vel_y >= 0:
					self.dy = tile[1].top - self.rect.bottom
					self.vel_y = 0
					self.on_ground = True
					self.in_the_air = False
					self.wall = False #澤木
		
		#壁に接触した瞬間跳ね返る(澤木)
		if self.wall:
			self.dx *= -1

	#重力の設定メソッド
	def add_gravity(self):
		#重力設定、y軸速度を加速してdyにプラスする
		self.vel_y += 1
		if self.vel_y > 10:
			self.vel_y = 10
		self.dy += self.vel_y

		#y軸速度が0でなければ、フラグをtrueにする。
		# 接触判定で地面と接触している時はy軸速度を0にするので、
        # y軸速度が0でないということは、空中にいるということです。
		if self.vel_y != 0:
			self.in_the_air = True
		elif self.vel_y > 0:
			self.UP,self.DOWN = False, True
			
	#描画用メソッド
	def draw(self):
		#プレイヤーをスクリーンに描画(directioonの 0 か 1 で左右を判定)
		if self.direction == 0:
			self.image = self.right_image
		if self.direction == 1:
			self.image = self.left_image
		SCREEN.blit(self.image,(self.rect.x,self.rect.y))	

	#updateメソッドに処理をまとめる
	def update(self,data):
		self.key_con(data)
		self.draw()


#ゲームクラス	
class Game():
	def __init__(self):
		pg.init()

		#クラスのインスタンス化
		self.stage = Stage(stage_data)
		self.player = Player(100, 200)
		#スプライトクラス設定してプレイヤーを追加
		self.playerSprite = pg.sprite.GroupSingle(self.player)

		#バックグラウンド画像の呼び出し、サイズ設

	#溝に落ちた際に実行するメソッド
	def respawn(self):
		self.player = Player(100, 0)
		self.playerSprite.add(self.player)
	
	#メインループ処理
	def main(self):
<<<<<<< HEAD:ex06/相澤.py
		bg = pg.image.load('ex06/img/BG2.png').convert()
=======
		bg = pg.image.load('ex06/pic/night1.png').convert()
>>>>>>> 3a274bf02a1decce3d4a7055b4edb83bb375d07a:ex06/jump4.py
		bg = pg.transform.scale(bg,(screen_width,screen_height))
		global bg_y
		running = True
		while running:	
			for event in pg.event.get():
				if event.type == pg.QUIT:
					running = False
				if event.type == pg.KEYDOWN:
					if event.key == pg.K_ESCAPE:
						running = False
			
			#画面の初期化
			SCREEN.fill((55,100,200))
			
			#背景を描画
			#SCREEN.blit(self.bg,(0,0))
			#ステージの描画
			bg_y = (bg_y+0.4)%screen_height
			SCREEN.blit(bg,[0,bg_y])
			SCREEN.blit(bg,[0,bg_y-screen_height])
			self.stage.draw()

			#プレイヤーが画面の端周辺に来た場合にバックグラウンド側を動かす処理（左右）
			if self.player.rect.x > RIGHT_EDGE and self.player.RIGHT:
				self.stage.scroll_front()
				#バックグラウンドが動いている時にプレイヤーが物体にぶつかると強制的に移動してしまうので、調整。
				if self.player.collisionX:
					self.player.rect.x -= 5

			#上記と同じ（左右反対の処理）
			elif self.player.rect.x < LEFT_EDGE and self.player.LEFT:
				self.stage.scroll_back()
				if self.player.collisionX:
					self.player.rect.x += 5
			
			#プレイヤーが画面の端周辺に来た場合にバックグラウンド側を動かす処理(上下)
			if self.player.rect.y > UP_EDGE and self.player.UP:
				self.stage.scroll_head()
				#バックグラウンドが動いている時にプレイヤーが物体にぶつかると強制的に移動してしまうので、調整。
				if self.player.collisionY:
					self.player.rect.y -= 5
		
			#上記と同じ（左右反対の処理）
			elif self.player.rect.y < DOWN_EDGE and self.player.DOWN:
				self.stage.scroll_foot()
				if self.player.collisionY:
					self.player.rect.y += 5
            
            
			
			#プレイヤーが溝に落っこちた時の処理
			if self.player.dead:
				self.respawn()
				self.player.dead = False

			#プレイヤーのメソッド呼び出し
			self.playerSprite.update(self.stage.tile_list)

			#クロック実行
			CLOCK.tick(FPS)
			pg.display.update()
			

		pg.quit()

#インスタンス化　→　実行
game = Game()
game.main()
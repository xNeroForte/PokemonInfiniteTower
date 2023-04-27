extends CharacterBody2D

const JUMP_VELOCITY = -400.0

func _ready():
	velocity = Vector2.ZERO # The player's movement vector.
	var screen_size = get_viewport_rect().size
func _physics_process(delta):
	var input_vector = Vector2.ZERO
	input_vector.x = Input.get_action_strength("ui_right") - Input.get_action_strength("ui_left")
	input_vector.y = Input.get_action_strength("ui_down") - Input.get_action_strength("ui_up")
	
	if input_vector != Vector2.ZERO:
		velocity = input_vector
	else:
		velocity = Vector2.ZERO
		
	move_and_collide(velocity)
#

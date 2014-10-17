require "gema"

describe Gema::MinimaxPlayer do
before :each do
@mp = Gema::MinimaxPlayer.new("X")
end

it "Debe existir un metodo move" do
@mp.respond_to?("move").should == true
end

it "El metodo move debe tratar de evitar la derrota" do
@board = Gema::Board.new(["X", "X", "O", "O", "O", "X", " ", "O", " "])
@mp.move(@board).should == "c1"
  end

it "El metodo move debe tratar de ganar" do
@board = Gema::Board.new([" ", "O", "X", " ", "X", " ", "O", "O", "X"])
@mp.move(@board).should == "a1"
  end
end

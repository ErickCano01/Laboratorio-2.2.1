using System;

public class Tareas {
	private int id;
	private int prioridad;
	private String contexto;

	public void SetContexto(ref object contexto) {
		throw new System.NotImplementedException("Not implemented");
	}
	public int GetId() {
		return this.id;
	}
	public void SetId(ref int id) {
		this.id = id;
	}
	public int GetPrioridad() {
		return this.prioridad;
	}
	public void SetPrioridad(ref int prioridad) {
		this.prioridad = prioridad;
	}
	public String GetContexto() {
		return this.contexto;
	}
	public void SetContexto(ref String contexto) {
		this.contexto = contexto;
	}

	private Integrante encargado;


}
